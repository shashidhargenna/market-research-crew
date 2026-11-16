import pandas as pd
from crewai.tools import tool


@tool("Financial Data Parser")
def calculate_financial_metrics(csv_path: str) -> str:
    """
    Loads financial metrics from a CSV file,
    calculates statistical summaries and returns
    the results as a Markdown table.
    """

    try:
        # Load CSV into a Pandas DataFrame
        df = pd.read_csv(csv_path)

        # Select numerical columns
        numeric_df = df.select_dtypes(include="number")

        if numeric_df.empty:
            return "No numerical columns found in the CSV file."

        # Calculate statistical summaries
        summary = numeric_df.describe()

        # Convert results into Markdown
        markdown_table = summary.to_markdown()

        return markdown_table

    except FileNotFoundError:
        return f"CSV file not found: {csv_path}"

    except Exception as e:
        return f"Error processing financial data: {str(e)}"