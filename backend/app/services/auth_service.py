"""
File: auth_service.py
Purpose: Minimal User Authentication Service.
         Password hashing (sha256+salt), JWT/Session token creation, and User retrieval.
Module: Backend / Services
"""

import hashlib
import hmac
import secrets
import json
import base64
from typing import Optional, Dict, Any
from sqlmodel import Session, select
from backend.app.models.user import User

SECRET_KEY = "healthlens-secret-key-change-in-production"

def hash_password(password: str, salt: Optional[str] = None) -> str:
    if not salt:
        salt = secrets.token_hex(8)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000).hex()
    return f"{salt}${pw_hash}"

def verify_password(password: str, stored_hash: str) -> bool:
    try:
        salt, pw_hash = stored_hash.split('$')
        computed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000).hex()
        return hmac.compare_digest(pw_hash, computed)
    except Exception:
        return False

def create_token(user_id: int, email: str) -> str:
    payload = {"user_id": user_id, "email": email}
    payload_bytes = json.dumps(payload).encode('utf-8')
    b64_payload = base64.b64encode(payload_bytes).decode('utf-8')
    signature = hmac.new(SECRET_KEY.encode('utf-8'), b64_payload.encode('utf-8'), hashlib.sha256).hexdigest()
    return f"{b64_payload}.{signature}"

def decode_token(token: str) -> Optional[Dict[str, Any]]:
    try:
        b64_payload, signature = token.split('.')
        expected_sig = hmac.new(SECRET_KEY.encode('utf-8'), b64_payload.encode('utf-8'), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(signature, expected_sig):
            return None
        payload_bytes = base64.b64decode(b64_payload.encode('utf-8'))
        return json.loads(payload_bytes.decode('utf-8'))
    except Exception:
        return None

class AuthService:
    def register(self, db_session: Session, email: str, password: str, name: str, age: int = 30, gender: str = "other", pregnant: bool = False, preferred_language: str = "en") -> Dict[str, Any]:
        # Check if user exists
        stmt = select(User).where(User.email == email)
        existing = db_session.exec(stmt).first()
        if existing:
            raise ValueError("Email already registered")

        pw_hash = hash_password(password)
        user = User(
            email=email,
            password_hash=pw_hash,
            name=name,
            age=age,
            gender=gender,
            pregnant=pregnant,
            preferred_language=preferred_language
        )
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        token = create_token(user.id, user.email)
        return {
            "token": token,
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "age": user.age,
                "gender": user.gender,
                "preferred_language": user.preferred_language
            }
        }

    def login(self, db_session: Session, email: str, password: str) -> Dict[str, Any]:
        stmt = select(User).where(User.email == email)
        user = db_session.exec(stmt).first()
        if not user or not user.password_hash or not verify_password(password, user.password_hash):
            raise ValueError("Invalid email or password")

        token = create_token(user.id, user.email)
        return {
            "token": token,
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "age": user.age,
                "gender": user.gender,
                "preferred_language": user.preferred_language
            }
        }

    def get_user_from_token(self, db_session: Session, token: str) -> Optional[User]:
        decoded = decode_token(token)
        if not decoded or "user_id" not in decoded:
            return None
        return db_session.get(User, decoded["user_id"])

auth_service = AuthService()
