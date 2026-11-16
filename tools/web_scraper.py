import os
import requests

from bs4 import BeautifulSoup
from tavily import TavilyClient
from dotenv import load_dotenv
from crewai.tools import tool

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


load_dotenv()


# --------------------------------------------------
# 1. Configure HTTP retry mechanism
# --------------------------------------------------

def create_session():

    session = requests.Session()

    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
        respect_retry_after_header=True
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)

    session.mount("https://", adapter)
    session.mount("http://", adapter)

    return session


# --------------------------------------------------
# 2. Extract publication date from HTML metadata
# --------------------------------------------------

def extract_publication_date(soup):

    date_selectors = [
        {"property": "article:published_time"},
        {"property": "og:published_time"},
        {"name": "pubdate"},
        {"name": "publishdate"},
        {"name": "date"},
        {"itemprop": "datePublished"}
    ]

    for selector in date_selectors:

        tag = soup.find("meta", attrs=selector)

        if tag and tag.get("content"):
            return tag["content"]

    # Check time elements
    time_tag = soup.find("time")

    if time_tag:

        return (
            time_tag.get("datetime")
            or time_tag.get_text(strip=True)
        )

    return "Publication date not available"


# --------------------------------------------------
# 3. Extract readable webpage content
# --------------------------------------------------

def extract_page_content(html):

    soup = BeautifulSoup(html, "html.parser")

    publication_date = extract_publication_date(soup)

    # Remove unnecessary elements
    for element in soup(
        [
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "aside",
            "noscript"
        ]
    ):

        element.decompose()

    # Prefer article content when available
    content_container = (
        soup.find("article")
        or soup.find("main")
        or soup.body
        or soup
    )

    page_text = content_container.get_text(
        separator=" ",
        strip=True
    )

    # Limit extracted webpage content
    page_text = page_text[:8000]

    return page_text, publication_date


# --------------------------------------------------
# 4. Main CrewAI Web Scraper Tool
# --------------------------------------------------

@tool("Web Scraper Tool")
def scrape_market_research(query: str) -> str:
    """
    Searches the web using Tavily, extracts search metadata,
    retrieves webpage content using Requests and BeautifulSoup,
    preserves Tavily fallback content, extracts publication dates,
    handles HTTP failures, and returns structured research evidence.
    """

    session = None

    try:

        # Step 1: Get Tavily API key

        api_key = os.getenv("TAVILY_API_KEY")

        if not api_key:

            return "ERROR: TAVILY_API_KEY is missing."

        # Step 2: Initialize Tavily

        tavily = TavilyClient(api_key=api_key)

        # Step 3: Search the internet

        search_results = tavily.search(
            query=query,
            max_results=5
        )

        results = search_results.get("results", [])

        if not results:

            return "No search results found."

        # Step 4: Create HTTP session

        session = create_session()

        scraped_data = []

        visited_urls = set()

        # Step 5: Process each search result

        for index, result in enumerate(results, start=1):

            url = result.get("url")

            if not url or url in visited_urls:
                continue

            visited_urls.add(url)

            title = result.get("title", "Unknown")

            # Tavily search metadata
            tavily_content = result.get("content", "")

            relevance_score = result.get("score", "Not available")

            published_date = (
                result.get("published_date")
                or "Not available"
            )

            page_text = ""

            webpage_date = "Not available"

            scraping_status = "Not attempted"

            # Step 6: Identify PDF documents

            is_pdf = (
                url.lower().split("?")[0].endswith(".pdf")
            )

            if is_pdf:

                scraping_status = (
                    "PDF detected. HTML extraction skipped."
                )

            else:

                try:

                    # Step 7: Download webpage

                    response = session.get(
                        url,
                        timeout=(5, 15),
                        headers={
                            "User-Agent": "Mozilla/5.0"
                        }
                    )

                    response.raise_for_status()

                    content_type = response.headers.get(
                        "Content-Type", ""
                    ).lower()

                    if "text/html" in content_type or not content_type:

                        # Step 8: Extract HTML content

                        page_text, webpage_date = extract_page_content(
                            response.content
                        )

                        if page_text:

                            scraping_status = (
                                "HTML content extracted successfully."
                            )

                        else:

                            scraping_status = (
                                "HTML downloaded, but no readable content extracted."
                            )

                    else:

                        scraping_status = (
                            f"Unsupported content type: {content_type}"
                        )

                except requests.RequestException as e:

                    scraping_status = (
                        f"Webpage scraping failed: {str(e)}"
                    )

            # Step 9: Preserve both content sources

            if not page_text and not tavily_content:

                continue

            scraped_data.append(
                f"""
==================================================
SOURCE {index}
==================================================

Title:
{title}

URL:
{url}

Tavily Relevance Score:
{relevance_score}

Tavily Publication Date:
{published_date}

Webpage Publication Date:
{webpage_date}

Scraping Status:
{scraping_status}


---------------- TAVILY SEARCH CONTENT ----------------

{tavily_content or "No Tavily content available."}


---------------- SCRAPED WEBPAGE CONTENT ----------------

{page_text or "No webpage content extracted."}

==================================================
"""
            )

        # Step 10: Close HTTP session

        if not scraped_data:

            return (
                "No usable research content could be extracted "
                "from the search results."
            )

        return "\n\n".join(scraped_data)

    except Exception as e:

        return f"Web scraping failed: {str(e)}"

    finally:

        if session:

            session.close()