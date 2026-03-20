from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import FileResponse

from app.services.search_service import get_market_data
from app.services.ai_service import analyze_market
from app.security.auth import verify_api_key
from app.security.rate_limit import limiter
from app.utils.logger import logger
from app.utils.report_writer import save_markdown_report

# Router instance for sector analysis endpoints
router = APIRouter()


@router.get("/analyze/{sector}")
@limiter.limit("3/minute")  # Rate limit to prevent abuse / excessive AI API usage
async def analyze_sector(
    request: Request,
    sector: str,
    api_key: str = Depends(verify_api_key)  # API key verification for security
):

    # Normalize input to avoid case mismatch issues in search / file naming
    sector = sector.strip().lower()

    logger.info(f"Request received for sector: {sector}")

    # Basic validation to avoid invalid / empty sector values
    if not sector or len(sector) < 2:
        raise HTTPException(400, "Invalid sector")

    # Fetch market data from external search / scraping service
    # This keeps router clean and follows service-layer architecture
    data = get_market_data(sector)

    # If no data found, return 404 instead of empty AI response
    if not data:
        raise HTTPException(404, "No data found")

    # AI analysis step (LLM / API call handled in service layer)
    # Keeping AI logic outside router improves maintainability
    report = analyze_market(sector, data)

    # Save report as markdown file for download feature
    # Writing to file allows persistence and reproducibility
    save_markdown_report(sector, report)

    # Local download endpoint for generated report
    download_url = f"http://127.0.0.1:8000/download/{sector}"

    # Structured response for frontend / Swagger / API consumers
    return {
        "sector": sector,
        "current_trend": report.get("current_trend", ""),
        "recent_events": report.get("recent_events", []),
        "market_performance": report.get("market_performance", ""),
        "investment_outlook": report.get("investment_outlook", ""),
        "risks": report.get("risks", []),
        "opportunities": report.get("opportunities", []),
        "download_file": download_url
    }


@router.get("/download/{sector}")
def download_report(
    sector: str,
    api_key: str = Depends(verify_api_key)  # Protect download with API key
):

    # Normalize again to match saved filename format
    sector = sector.strip().lower()

    # Reports are stored in reports/ directory with fixed naming convention
    path = f"reports/{sector}_report.md"

    # FileResponse streams file instead of loading fully into memory
    # Better for performance and large files
    return FileResponse(
        path,
        media_type="text/markdown",
        filename=f"{sector}_report.md"
    )