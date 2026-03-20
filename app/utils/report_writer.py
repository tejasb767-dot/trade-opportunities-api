import os


def save_markdown_report(sector: str, report: dict):

    # File name based on sector for easy identification
    filename = f"{sector}_report.md"

    # Markdown template for report file
    content = f"""
# Sector Analysis Report

## Sector
{sector}

## Current Trend
{report.get("current_trend")}

## Recent Events
"""

    for e in report.get("recent_events", []):
        content += f"- {e}\n"

    content += f"""

## Market Performance
{report.get("market_performance")}

## Investment Outlook
{report.get("investment_outlook")}

## Risks
"""

    for r in report.get("risks", []):
        content += f"- {r}\n"

    content += "\n## Opportunities\n"

    for o in report.get("opportunities", []):
        content += f"- {o}\n"

    # Reports stored inside /reports folder
    path = os.path.join("reports", filename)

    # Ensure folder exists before writing file
    os.makedirs("reports", exist_ok=True)

    # Write markdown file
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path