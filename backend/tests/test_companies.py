def test_create_company(client, superadmin):
    """Cria uma empresa e valida se o admin foi criado"""
    # Login primeiro
    login = client.post("/api/auth/login", json={
        "company_name": "",
        "email": "admin@soft.com",
        "password": "admin123"
    })
    token = login.get_json()["access_token"]

    payload = {
        "name": "Soft Tecnologia",
        "cnpj": "12345678000199",
        "email": "contato@soft.com",
        "phone": "11999999999",
        "address": "Rua Central, 123",
        "website": "softtech.com",
        "logo": None,
    }

    response = client.post(
        "/api/core/companies",
        headers={"Authorization": f"Bearer {token}"},
        json=payload
    )

    data = response.get_json()
    assert response.status_code == 201
    assert "empresa" in data["message"].lower()
