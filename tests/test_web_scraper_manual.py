from tools.web_scraper import scrape_market_research

result = scrape_market_research.run(
    "Latest financial performance and revenue of Apple Inc."
)

print("\nWEB SCRAPER RESULT:\n")
print(result)
