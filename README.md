AI-Powered Market Research and Financial Analysis System

1. Project Overview

This project is an AI-powered market research and financial analysis application built using CrewAI.

It uses multiple AI agents working together in a hierarchical workflow to research a company’s financial performance, analyze financial datasets, and generate a structured market research report.

The application combines web research, financial data analysis, and automated report generation to produce reports in Markdown and PDF formats.

2. Key Features

* Automated Web Research: Uses Tavily to search for company financial information and market trends.
* Web Scraping: Extracts webpage content using Requests and BeautifulSoup.
* Publication Date Extraction: Retrieves publication dates from webpage metadata where available.
* Financial Data Analysis: Uses Pandas to calculate statistical metrics from CSV datasets.
* Multi-Agent Collaboration: Uses specialized Researcher, Analyst, and Writer agents.
* Hierarchical Workflow: Uses a manager LLM to coordinate task execution.
* Automated Report Generation: Generates structured Markdown and PDF reports.
* Error Handling: Includes HTTP retries, fallback search content, and exception handling.

3. Technology Stack

Technology	Purpose
Python	Core programming language
CrewAI	Multi-agent orchestration
Tavily	Web search
Requests	HTTP requests
BeautifulSoup	HTML parsing and content extraction
Pandas	Financial data analysis
ReportLab	PDF generation
python-dotenv	Environment variable management

4. Project Architecture

The application consists of three specialized AI agents.

Researcher Agent

* Searches the web for company financial information and market developments.
* Uses the Web Scraper Tool to retrieve webpage content.
* Identifies financial metrics, reporting periods, and supporting evidence.
* Distinguishes reported financial results from historical information and forecasts.

Analyst Agent

* Reads financial data from a CSV file.
* Uses Pandas to perform statistical analysis.
* Calculates count, mean, minimum, maximum, standard deviation, quartiles, and median.
* Treats the CSV as an independent sample dataset.

Writer Agent

* Uses the Researcher and Analyst task outputs.
* Combines the findings into a structured market research report.
* Generates sections covering company information, financial performance, market trends, key findings, and conclusions.

Hierarchical Process

The crew uses CrewAI’s hierarchical process.

A manager LLM coordinates the agents and their tasks to produce the final report.

5. Project Folder Structure

market-research-crew/
│
├── config/
│   └── config.py
│
├── crew/
│   ├── agents.py
│   ├── tasks.py
│   └── crew.py
│
├── tools/
│   ├── web_scraper.py
│   └── financial_parser.py
│
├── outputs/
│   ├── sample_financials.csv
│   ├── market_research_report.md
│   └── market_research_report.pdf
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

6. Installation and Setup

Step 1: Clone the Repository

git clone <your-github-repository-url>
cd market-research-crew

Step 2: Create a Virtual Environment

python -m venv venv

Activate the environment.

For macOS/Linux:

source venv/bin/activate

For Windows:

venv\Scripts\activate

Step 3: Install Dependencies

pip install -r requirements.txt

7. Environment Variables

Create a .env file in the project root directory.

Add the required API credentials:

TAVILY_API_KEY=your_tavily_api_key
# Add the LLM provider API key required by config/config.py

Make sure not to expose API keys or other sensitive credentials in the repository.

8. How to Run

Execute the application using:

python main.py

The application takes the company research query, CSV file path, and current date as inputs.

Example:

inputs = {
    "query": "Apple Inc. (AAPL) financial performance and market trends",
    "csv_path": "outputs/sample_financials.csv",
    "current_date": date.today().isoformat()
}

After successful execution, the application generates:

* outputs/market_research_report.md
* outputs/market_research_report.pdf

9. Workflow

The application follows this workflow:

1. The user provides a company research query and CSV dataset.
2. The Researcher Agent searches the web and extracts relevant information.
3. The Analyst Agent processes the CSV dataset and calculates statistical metrics.
4. The Writer Agent uses the outputs of the Researcher and Analyst to prepare the report.
5. The hierarchical manager coordinates the crew’s execution.
6. The final report is saved in Markdown and PDF formats.

10. Sample Analysis

The application analyzes a sample financial dataset containing Revenue and Profit columns.

The Analyst calculates:

* Count
* Mean
* Minimum
* Maximum
* Standard deviation
* First quartile (Q1)
* Median
* Third quartile (Q3)

The sample dataset is analyzed independently and is not treated as verified company financial information.

11. Known Limitations

* Search results depend on the availability and relevance of information returned by Tavily.
* Web scraping may fail when websites restrict automated requests or return unsupported content.
* PDF documents are detected, but their contents are not currently extracted.
* Publication dates may not be available in webpage metadata.
* Retrieved financial figures are not independently verified against official financial statements.
* The accuracy of the final report depends on the quality of retrieved information and agent outputs.

12. Future Improvements

* Integrate official financial data sources such as SEC filings and company investor relations.
* Implement PDF text extraction.
* Add structured financial data validation.
* Improve source ranking and retrieval.
* Add automated evaluation of agent outputs.
* Introduce more robust citation and evidence validation.

13. Conclusion

This project demonstrates how CrewAI can coordinate specialized AI agents to automate market research, financial data analysis, and report generation through a hierarchical multi-agent architecture.