"""
Unit tests for Minimal User Authentication (AuthService & API endpoints).
"""

import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_register_and_login_flow():
    email = f"test_{pytest.importorskip('secrets').token_hex(4)}@healthlens.ai"
    password = "SecurePassword123!"

    # 1. Register
    reg_res = client.post(
        "/api/v1/auth/register",
        json={
            "email": email,
            "password": password,
            "name": "Test User",
            "age": 32,
            "gender": "female"
        }
    )
    assert reg_res.status_code == 200
    reg_data = reg_res.json()["data"]
    assert "token" in reg_data
    assert reg_data["user"]["email"] == email

    token = reg_data["token"]

    # 2. Get me profile
    me_res = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert me_res.status_code == 200
    me_data = me_res.json()["data"]
    assert me_data["email"] == email
    assert me_data["name"] == "Test User"

    # 3. Login
    login_res = client.post(
        "/api/v1/auth/login",
        json={"email": email, "password": password}
    )
    assert login_res.status_code == 200
    login_data = login_res.json()["data"]
    assert "token" in login_data

def test_duplicate_registration_fails():
    email = "duplicate@healthlens.ai"
    password = "Pass123!Password"

    res1 = client.post(
        "/api/v1/auth/register",
        json={"email": email, "password": password, "name": "Dup User", "age": 28, "gender": "male"}
    )
    assert res1.status_code == 200

    # Duplicate should fail with 400
    res2 = client.post(
        "/api/v1/auth/register",
        json={"email": email, "password": password, "name": "Dup User 2", "age": 28, "gender": "male"}
    )
    assert res2.status_code == 400

def test_invalid_login_credentials():
    login_res = client.post(
        "/api/v1/auth/login",
        json={"email": "nonexistent@healthlens.ai", "password": "WrongPassword"}
    )
    assert login_res.status_code == 401
