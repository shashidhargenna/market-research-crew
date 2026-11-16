from pathlib import Path
from crew.crew import run_market_research
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from xml.sax.saxutils import escape
import re
from datetime import date

def generate_pdf_report(markdown_path, pdf_path):

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=20,
        textColor=colors.darkblue,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=colors.darkblue,
        spaceBefore=15,
        spaceAfter=8
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["BodyText"],
        fontSize=9,
        leading=14,
        spaceAfter=8
    )

    story = []

    with open(markdown_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:

        line = line.strip()

        if not line:
            story.append(Spacer(1, 6))
            continue

        if line.startswith("# "):
            text = escape(line[2:])
            story.append(Paragraph(text, title_style))

        elif line.startswith("## "):
            text = escape(line[3:])
            story.append(Paragraph(text, heading_style))

        elif line.startswith("### "):
            text = escape(line[4:])
            story.append(Paragraph(text, styles["Heading3"]))

        elif line.startswith("- "):
            text = escape(line[2:])
            story.append(
                Paragraph(
                    f"&bull; {text}",
                    body_style
                )
            )

        else:
            text = escape(line)

            # Convert Markdown bold formatting
            text = re.sub(
                r"\*\*(.*?)\*\*",
                r"<b>\1</b>",
                text
            )

            # Convert Markdown links
            text = re.sub(
                r"\[(.*?)\]\((https?://[^)]+)\)",
                r'<link href="\2" color="blue">\1</link>',
                text
            )

            story.append(
                Paragraph(text, body_style)
            )

    doc.build(story)

    print(f"PDF generated successfully: {pdf_path}")
    
    
    
def main():

    inputs = {

    "query": "Apple Inc. (AAPL) financial performance and market trends",

    "csv_path": "outputs/sample_financials.csv",

    "current_date": date.today().isoformat()

}

    print("\nSTARTING MARKET RESEARCH CREW...\n")

    result = run_market_research(inputs)

    print("\nFINAL MARKET RESEARCH REPORT:\n")

    print(result)

    # Save the final report
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    report_path = output_dir / "market_research_report.md"

    report_path.write_text(str(result), encoding="utf-8")

    print(f"\nReport saved successfully at: {report_path}")

# Generate PDF report
    pdf_path = output_dir / "market_research_report.pdf"

    generate_pdf_report(report_path, pdf_path)

if __name__ == "__main__":
    main()