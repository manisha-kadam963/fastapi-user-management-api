from fastapi import Depends, HTTPException
from app.auth import verify_token

def get_current_user(token: str):
    try:
        data = verify_token(token)
        return data
    except:
        raise HTTPException(status_code=401, detail="Invalid token")