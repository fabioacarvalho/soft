def test_permission_decorator_denied(client, seller):
    login = client.post("/api/auth/login", json={
        "company_name": "",
        "email": seller.email,
        "password": "seller123"
    })
    token = login.get_json()["access_token"]

    res = client.put(
        "/api/sales/leads/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 403


def test_permission_decorator_allowed(client, superadmin):
    login = client.post("/api/auth/login", json={
        "company_name": "",
        "email": "admin@soft.com",
        "password": "admin123"
    })
    token = login.get_json()["access_token"]

    res = client.put(
        "/api/sales/leads/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code != 403
