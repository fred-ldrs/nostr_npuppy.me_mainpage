from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from . import models, auth, address, config

app = FastAPI(title="npuppy.me - NOSTR Address Service")

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers from other modules
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(address.router, prefix="/address", tags=["Address Management"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to npuppy.me NOSTR Address Service API",
        "version": "1.0.0",
        "documentation": "/docs",
    }

@app.get("/.well-known/nostr.json")
async def nostr_well_known():
    """
    Implements the .well-known standard for NOSTR domain verification
    """
    # This would be expanded to dynamically generate entries from the database
    return {
        "names": {
            # Example entry - this would come from your database
            "example": "npub1abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnop"
        }
    }

# For Vercel serverless functions
handler = app
