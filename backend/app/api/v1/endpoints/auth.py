# --------------------------------------------------
# File: auth.py
# Purpose: Minimal User Authentication API Endpoints (/register, /login, /me).
# Module: API Engine / Endpoints
# Used By: Frontend Auth Provider & Navigation
# --------------------------------------------------

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Header, status
from pydantic import BaseModel, EmailStr
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.services.auth_service import auth_service
from backend.app.schemas.base import BaseResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    name: str
    age: int = 30
    gender: str = "other"
    pregnant: bool = False
    preferred_language: str = "en"

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/register", summary="Register New User Account")
async def register_user_endpoint(
    payload: RegisterRequest,
    db_session: Session = Depends(get_db_session),
):
    try:
        data = auth_service.register(
            db_session,
            email=payload.email,
            password=payload.password,
            name=payload.name,
            age=payload.age,
            gender=payload.gender,
            pregnant=payload.pregnant,
            preferred_language=payload.preferred_language,
        )
        return BaseResponse(success=True, data=data, message="Registration successful.")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", summary="Login User Account")
async def login_user_endpoint(
    payload: LoginRequest,
    db_session: Session = Depends(get_db_session),
):
    try:
        data = auth_service.login(db_session, email=payload.email, password=payload.password)
        return BaseResponse(success=True, data=data, message="Login successful.")
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.get("/me", summary="Get Current Authenticated User Profile")
async def get_current_user_endpoint(
    authorization: Optional[str] = Header(None),
    db_session: Session = Depends(get_db_session),
):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authentication token required")
    
    token = authorization.replace("Bearer ", "").strip()
    user = auth_service.get_user_from_token(db_session, token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return BaseResponse(
        success=True,
        data={
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "age": user.age,
            "gender": user.gender,
            "preferred_language": user.preferred_language
        },
        message="User profile retrieved."
    )
