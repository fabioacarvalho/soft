def test_me_permissions_superadmin(client, superadmin):
    login = client.post("/api/auth/login", json={
        "company_name": "",
        "email": "admin@soft.com",
        "password": "admin123"
    })

    token = login.get_json()["access_token"]

    res = client.get(
        "/api/auth/me/permissions",
        headers={"Authorization": f"Bearer {token}"}
    )

    data = res.get_json()

    assert res.status_code == 200
    assert data["role"] == "superadmin"
    assert "*" in data["permissions"]
