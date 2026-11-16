from crewai import Task

from crew.agents import researcher, analyst, writer

# =====================================================
# TASK 1: MARKET RESEARCH
# =====================================================

research_task = Task(

    description=(

        "Conduct comprehensive and evidence-based market research "
        "for the following query: {query}.\n\n"

        "The current date is {current_date}.\n\n"

        "You MUST use the Web Scraper Tool to retrieve research "
        "information. Do not rely exclusively on your internal knowledge.\n\n"

        # ==========================================
        # RESEARCH PRIORITIES
        # ==========================================

        "RESEARCH PRIORITIES:\n\n"

        "1. Identify the company name, stock ticker, and relevant "
        "business sector.\n"

        "2. Search for the latest available officially reported "
        "quarterly and annual financial results.\n"

        "3. Prioritize information published within the last "
        "12 months relative to {current_date}, where available.\n"

        "4. Prioritize official company investor relations releases, "
        "annual reports, quarterly reports, and SEC filings.\n"

        "5. Use reputable financial news sources and analyst reports "
        "as secondary sources.\n"

        "6. Do not assume that the newest article contains the "
        "newest financial reporting period.\n"

        "7. Evaluate the reporting period of each financial result "
        "separately from its publication date.\n\n"

        # ==========================================
        # FINANCIAL INFORMATION
        # ==========================================

        "FINANCIAL INFORMATION TO COLLECT:\n\n"

        "Identify the following metrics when available:\n"

        "- Revenue\n"
        "- Net income\n"
        "- Earnings per share (EPS)\n"
        "- Gross margin\n"
        "- Operating income\n"
        "- Profit margin\n"
        "- Year-over-year revenue growth\n"
        "- Other important officially reported financial metrics.\n\n"

        "For every financial figure, identify:\n"

        "- Metric name.\n"
        "- Exact reported value.\n"
        "- Currency and units.\n"
        "- Fiscal year or quarter.\n"
        "- Reporting period end date, if available.\n"
        "- Source title.\n"
        "- Source publication date, if available.\n"
        "- Source URL.\n"
        "- Supporting evidence from the retrieved source content.\n"

        "If any of these details are unavailable, explicitly "
        "identify the missing information.\n\n"

        # ==========================================
        # SOURCE EVIDENCE
        # ==========================================

        "SOURCE EVIDENCE RULES:\n\n"

        "1. Every financial figure must have supporting evidence "
        "in the content returned by the Web Scraper Tool.\n"

        "2. Do not assume that a figure is supported merely because "
        "a source URL is available.\n"

        "3. Do not claim that a source confirms a figure unless "
        "the retrieved content actually supports that figure.\n"

        "4. Distinguish information extracted directly from a source "
        "from information that is merely mentioned in a search snippet.\n"

        "5. Prefer official company filings and announcements "
        "when reporting company financial results.\n"

        "6. Do not treat a stock quote page as sufficient evidence "
        "for detailed financial statements.\n"

        "7. Do not treat analyst opinions or forecasts as "
        "officially reported company results.\n"

        "8. Include only URLs actually returned by the "
        "Web Scraper Tool.\n"

        "9. Never invent source names, URLs, publication dates, "
        "financial figures, or supporting quotations.\n\n"

        # ==========================================
        # HISTORICAL DATA AND FORECASTS
        # ==========================================

        "HISTORICAL DATA AND FORECAST RULES:\n\n"

        "1. Clearly distinguish current reported results "
        "from historical financial results.\n"

        "2. Identify the reporting period for every historical figure.\n"

        "3. Clearly label analyst estimates and projections "
        "as forecasts.\n"

        "4. Never present forecast figures as actual reported results.\n"

        "5. Do not describe historical financial results as "
        "the latest available results without establishing "
        "that no newer reporting period was found.\n"

        "6. If newer financial results cannot be retrieved, "
        "explicitly state that the latest available result "
        "could not be established from the retrieved sources.\n\n"

        # ==========================================
        # MARKET TRENDS
        # ==========================================

        "MARKET TRENDS:\n\n"

        "1. Identify relevant technology and industry trends.\n"

        "2. Explain their relevance to the company only when "
        "supported by retrieved source evidence.\n"

        "3. Distinguish general industry developments from "
        "company-specific developments.\n"

        "4. Do not claim that a market trend will increase "
        "company revenue or profitability unless a source "
        "explicitly supports that conclusion.\n"

        "5. Do not introduce unrelated trends simply to "
        "make the report comprehensive.\n\n"

        # ==========================================
        # IMPORTANT DEVELOPMENTS
        # ==========================================

        "IMPORTANT DEVELOPMENTS:\n\n"

        "Identify relevant recent developments such as:\n"

        "- Product announcements.\n"
        "- Strategic partnerships.\n"
        "- Acquisitions.\n"
        "- Stock buyback announcements.\n"
        "- Regulatory developments.\n"
        "- Major business or operational changes.\n"

        "For each development, provide its announcement date "
        "and supporting source when available.\n"

        "Do not describe old announcements as recent developments.\n\n"

        # ==========================================
        # ACCURACY AND CONSISTENCY
        # ==========================================

        "ACCURACY AND CONSISTENCY RULES:\n\n"

        "1. Never invent financial figures or reporting periods.\n"

        "2. Never independently calculate missing financial figures.\n"

        "3. Preserve the original currency, units, and numerical values.\n"

        "4. Do not infer financial performance from unrelated "
        "industry statistics.\n"

        "5. Do not describe the company as financially strong, "
        "healthy, stable, or well-positioned without sufficient "
        "supporting evidence.\n"

        "6. Do not infer reasons for financial changes without "
        "supporting evidence.\n"

        "7. If two sources provide conflicting figures, preserve "
        "both figures and explicitly identify the disagreement.\n"

        "8. Do not silently select, correct, or reconcile "
        "conflicting information.\n"

        "9. Do not claim independent verification unless "
        "the research process actually establishes it.\n"

        "10. If information is unavailable, state "
        "'Information unavailable in retrieved sources'.\n\n"

        # ==========================================
        # FINAL RESEARCH OUTPUT
        # ==========================================

        "FINAL RESEARCH OUTPUT:\n\n"

        "Organize the findings into the following sections:\n\n"

        "1. Company Overview\n"

        "2. Latest Available Financial Performance\n"

        "3. Historical Financial Performance\n"

        "4. Revenue and Profitability\n"

        "5. Market Trends\n"

        "6. Important Recent Developments\n"

        "7. Analyst Estimates and Forecasts\n"

        "8. Source Evidence and References\n"

        "9. Information Gaps and Conflicting Findings\n\n"

        "For financial information, use structured entries "
        "containing the metric, value, reporting period, "
        "source URL, and supporting evidence.\n\n"

        "Conclude by explicitly identifying whether the "
        "latest available financial reporting period could "
        "be established from the retrieved evidence.\n"

    ),

    expected_output=(

        "A structured, evidence-based market research document "
        "containing company information, financial results, "
        "historical comparisons, market trends, developments, "
        "and analyst forecasts.\n\n"

        "Every financial figure must include its reporting period, "
        "source URL, and supporting evidence when available.\n\n"

        "Officially reported financial results must be separated "
        "from analyst estimates and projections.\n\n"

        "Publication dates must be distinguished from financial "
        "reporting period dates.\n\n"

        "Conflicting information and unavailable evidence must "
        "be explicitly identified.\n\n"

        "Only URLs returned by the Web Scraper Tool may be included."

    ),

    agent=researcher

)

# =====================================================
# TASK 2: FINANCIAL DATA ANALYSIS
# =====================================================

analysis_task = Task(

    description=(
        "Analyze the financial dataset available at {csv_path}.\n\n"

        "Use the Financial Data Parser tool to load and analyze "
        "the CSV using Pandas.\n\n"

        "Calculate:\n"
        "1. Count\n"
        "2. Mean\n"
        "3. Minimum\n"
        "4. Maximum\n"
        "5. Standard deviation\n"
        "6. 25th percentile\n"
        "7. Median\n"
        "8. 75th percentile\n\n"

        "STRICT DATA RULES:\n"

        "1. Treat the CSV as an independent sample dataset.\n"
        "2. Do not assume that the CSV contains Apple's actual "
        "financial statements.\n"
        "3. Do not describe CSV values as Apple's actual revenue "
        "or profit.\n"
        "4. Do not add financial ratios that were not calculated.\n"
        "5. Do not infer business performance from sample data.\n"
        "6. Do not make assumptions about Apple's financial health.\n"
        "7. Preserve calculated numerical values exactly.\n"
        "8. Clearly identify the CSV as the source.\n"
        "9. Explain only the statistical patterns present in the dataset.\n"
    ),

    expected_output=(
        "A statistical analysis of the supplied CSV containing:\n"
        "- Count\n"
        "- Mean\n"
        "- Minimum\n"
        "- Maximum\n"
        "- Standard deviation\n"
        "- Quartiles\n"
        "- Statistical explanations\n\n"

        "Clearly state that this is a sample dataset analysis "
        "and not verified Apple financial data."
    ),

    agent=analyst
)

# =====================================================
# TASK 3: REPORT WRITING
# =====================================================

writing_task = Task(

    description=(

        "Prepare a professional market research report using the "
        "research findings and financial analysis produced by the "
        "Researcher and Financial Data Analyst tasks.\n\n"

        "You MUST use the outputs of research_task and analysis_task "
        "as your exclusive sources of factual information.\n\n"

        # ==========================================
        # REPORT STRUCTURE
        # ==========================================

        "REPORT STRUCTURE:\n\n"

        "1. Executive Summary\n"
        "2. Company Overview\n"
        "3. Latest Financial Performance\n"
        "4. Financial Data Analysis\n"
        "5. Market Trends\n"
        "6. Important Developments\n"
        "7. Key Findings\n"
        "8. Conclusion\n"
        "9. Source References\n\n"

        # ==========================================
        # STRICT DATA ACCURACY RULES
        # ==========================================

        "STRICT DATA ACCURACY RULES:\n\n"

        "1. Use only facts explicitly provided by the Researcher "
        "and Financial Data Analyst tasks.\n"

        "2. Do not invent, modify, assume, estimate, or independently "
        "calculate financial figures.\n"

        "3. Preserve all numerical values exactly as provided "
        "in the previous task outputs.\n"

        "4. Every financial figure must be traceable to the "
        "Researcher or Financial Data Analyst output.\n"

        "5. Do not introduce financial metrics that are absent "
        "from the previous task outputs.\n"

        "6. Do not introduce external knowledge or information "
        "to fill gaps in the research.\n"

        "7. Preserve the original units, currencies, and reporting "
        "periods associated with financial figures.\n\n"

        # ==========================================
        # DATA SOURCE SEPARATION
        # ==========================================

        "DATA SOURCE SEPARATION RULES:\n\n"

        "8. Treat company research and CSV statistical analysis "
        "as two separate sources of information.\n"

        "9. Use the Researcher output for company financial results, "
        "market trends, company developments, and source references.\n"

        "10. Use the Financial Data Analyst output only for "
        "statistical analysis of the supplied CSV dataset.\n"

        "11. Never present sample CSV values as Apple's actual "
        "financial results.\n"

        "12. Do not describe sample CSV Revenue or Profit values "
        "as Apple's actual revenue or profit.\n"

        "13. Clearly label the CSV analysis as sample dataset "
        "statistical analysis.\n"

        "14. Do not combine sample CSV statistics with actual "
        "company financial results.\n\n"

        # ==========================================
        # SOURCE VERIFICATION
        # ==========================================

        "SOURCE VERIFICATION RULES:\n\n"

        "15. Include only URLs explicitly provided in the "
        "Researcher output.\n"

        "16. Never create, modify, or guess source URLs.\n"

        "17. Never invent publication dates or source names.\n"

        "18. Preserve publication dates exactly as provided.\n"

        "19. If a publication date is unavailable, write "
        "'Publication date unavailable'.\n"

        "20. Do not claim that a financial figure is independently "
        "verified unless the Researcher output provides supporting "
        "evidence.\n"

        "21. Distinguish between information reported by a source "
        "and information independently verified by the research process.\n\n"

        # ==========================================
        # REPORT CONTENT RULES
        # ==========================================

        "REPORT CONTENT RULES:\n\n"

        "22. Do not make unsupported claims about profitability, "
        "liquidity, operational efficiency, financial health, "
        "or competitive position.\n"

        "23. Do not infer reasons for revenue growth or profit changes "
        "unless those reasons are explicitly supported by the "
        "Researcher output.\n"

        "24. Do not introduce financial ratios that were not "
        "provided by the previous tasks.\n"

        "25. Do not create generic market trends or company "
        "developments to fill report sections.\n"

        "26. Do not describe the company as financially strong, "
        "stable, healthy, or well-positioned unless these "
        "descriptions are explicitly supported by the research.\n"

        "27. Do not predict future company performance unless "
        "the Researcher explicitly provides a forecast.\n"

        "28. Clearly distinguish analyst forecasts and estimates "
        "from officially reported financial results.\n"

        "29. Do not convert reported facts into unsupported "
        "business interpretations.\n"

        "30. Key findings and conclusions must be based strictly "
        "on the information available in the previous task outputs.\n\n"

        # ==========================================
        # HANDLING MISSING OR CONTRADICTORY DATA
        # ==========================================

        "MISSING AND CONTRADICTORY DATA RULES:\n\n"

        "31. If information required for a section is missing, "
        "write 'Information unavailable in the provided research'.\n"

        "32. If two financial figures or growth percentages "
        "appear inconsistent, explicitly flag the inconsistency.\n"

        "33. Never silently correct, reconcile, or choose between "
        "conflicting financial figures.\n"

        "34. Preserve the original figures and explain that "
        "the provided research contains an inconsistency.\n"

        "35. If a source does not provide sufficient evidence "
        "for a claim, do not present that claim as verified.\n\n"

        # ==========================================
        # FINAL QUALITY CHECK
        # ==========================================

        "FINAL QUALITY CHECK:\n\n"

        "36. Check that every financial figure matches its "
        "corresponding previous task output.\n"

        "37. Check that actual company financial results and "
        "sample CSV statistics are presented separately.\n"

        "38. Check that every source reference comes from "
        "the Researcher output.\n"

        "39. Check that reporting periods, currencies, and units "
        "are preserved.\n"

        "40. Ensure that no placeholders such as '[insert value]', "
        "'[description]', or '[source URL]' remain in the report.\n"

        "41. Ensure that all nine report sections are present.\n"

        "42. If information is unavailable, explicitly identify "
        "it instead of inventing content.\n"

        "43. Do not claim that all information has been verified "
        "or confirmed unless the previous task outputs establish it.\n"

    ),

    # ==========================================
    # EXPECTED OUTPUT
    # ==========================================

    expected_output=(

        "A complete professional market research report containing:\n\n"

        "1. Executive Summary\n"
        "2. Company Overview\n"
        "3. Latest Financial Performance\n"
        "4. Financial Data Analysis\n"
        "5. Market Trends\n"
        "6. Important Developments\n"
        "7. Key Findings\n"
        "8. Conclusion\n"
        "9. Source References\n\n"

        "The report must contain only information supported by "
        "the Researcher and Financial Data Analyst outputs.\n\n"

        "Actual company financial results must be separated from "
        "sample CSV statistical analysis.\n\n"

        "All financial figures, reporting periods, currencies, "
        "publication dates, and source URLs must match their "
        "original task outputs.\n\n"

        "Analyst estimates must be distinguished from reported "
        "financial results.\n\n"

        "Missing or contradictory information must be explicitly "
        "identified rather than silently corrected or invented.\n\n"

        "No fabricated financial figures, unsupported interpretations, "
        "invented references, or unfinished placeholders."

    ),

    agent=writer,

    context=[
        research_task,
        analysis_task
    ]

)
