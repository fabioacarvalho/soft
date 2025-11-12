from flask_jwt_extended import decode_token


def test_login_superadmin(client, superadmin):
    """Teste de login do superadmin"""
    payload = {
        "company_name": "",
        "email": "admin@soft.com",
        "password": "admin123"
    }

    response = client.post("/api/auth/login", json={
        "email": "admin@soft.com",
        "password": "admin123"
    })

    data = response.get_json()  # isso converte JSON em dict

    assert response.status_code == 200
    assert "access_token" in data
    decoded = decode_token(data["access_token"])
    assert decoded["sub"]["user_id"] == str(superadmin.id)
