from pydantic import BaseModel
from typing import List


# Response model for sector analysis API
# Using Pydantic ensures response validation, documentation, and type safety
class ReportResponse(BaseModel):

    # Sector name requested by user
    sector: str

    # AI generated summary of current market trend
    current_trend: str

    # Important recent events affecting the sector
    recent_events: List[str]

    # Overall performance description (growth / decline / stable)
    market_performance: str

    # AI-based investment suggestion / outlook
    investment_outlook: str

    # Possible risks in this sector
    risks: List[str]

    # Potential opportunities in this sector
    opportunities: List[str]