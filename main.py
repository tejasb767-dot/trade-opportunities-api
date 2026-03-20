from fastapi import FastAPI
from app.api.routes import router
from app.security.rate_limit import limiter

from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


# Main FastAPI application instance
app = FastAPI(
    title="Trade Opportunities API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach global rate limiter to app state
app.state.limiter = limiter

# Middleware required for SlowAPI rate limiting to work
app.add_middleware(SlowAPIMiddleware)


# Custom handler for rate limit errors
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded"}
    )


# Register API routes from router module
app.include_router(router)


# Health check / root endpoint
@app.get("/")
def root():
    return {"message": "API running"}