from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
import traceback
from mangum import Mangum

app = FastAPI(title="npuppy.me - NOSTR Address Service")

@app.get("/")
async def root():
    try:
        # Versuche die Module zu importieren
        import os
        import sys
        
        # Zum Debugging: Verzeichnisinhalte und Systempfad anzeigen
        dir_contents = os.listdir('.')
        api_contents = os.listdir('./api') if os.path.exists('./api') else ["api directory not found"]
        sys_path = sys.path
        
        # Versuche die Module zu importieren
        try:
            from api.models import models
            models_import = "Successful"
        except ImportError:
            models_import = traceback.format_exc()
            
        try:
            from api.auth import auth
            auth_import = "Successful"
        except ImportError:
            auth_import = traceback.format_exc()
        
        try:
            from api.address import address
            address_import = "Successful"
        except ImportError:
            address_import = traceback.format_exc()
        
        try:
            from api.config import config
            config_import = "Successful"
        except ImportError:
            config_import = traceback.format_exc()
        
        return {
            "message": "Debug Info for npuppy.me NOSTR Address Service API",
            "version": "1.0.0",
            "directory_contents": dir_contents,
            "api_directory_contents": api_contents,
            "sys_path": sys_path,
            "import_status": {
                "models": models_import,
                "auth": auth_import,
                "address": address_import,
                "config": config_import
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error: {str(e)}",
            "traceback": traceback.format_exc()
        }

# For Vercel serverless functions
handler = Mangum(app)
