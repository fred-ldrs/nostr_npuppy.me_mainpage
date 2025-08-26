from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

try:
    # Versuche relative Imports
    from .models import models
    from .auth import auth
    from .address import address
    from .config import config
except ImportError as e:
    # Falls ein Fehler auftritt, gib eine einfache Antwort zurück
    app = FastAPI(title="npuppy.me - NOSTR Address Service")
    
    @app.get("/")
    async def root():
        return {
            "status": "error",
            "message": f"Import error: {str(e)}"
        }
    
    handler = Mangum(app)
else:
    # Code wird nur ausgeführt, wenn keine ImportError auftritt
    app = FastAPI(title="npuppy.me - NOSTR Address Service")
    
    # Normale App-Konfiguration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
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
        return {
            "names": {
                "example": "npub1abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnop"
            }
        }
    
    handler = Mangum(app)
