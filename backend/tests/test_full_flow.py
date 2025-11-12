import pytest
from app import create_app, db
from app.models.core_model import User
from passlib.hash import sha256_crypt


@pytest.fixture
def app():
    """Cria o app Flask em modo de teste."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": "test-secret",
    })
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Cria o test client para enviar requisições HTTP."""
    return app.test_client()


@pytest.fixture
def superadmin(app):
    """Cria o superadmin no banco de testes."""
    admin = User(
        name="Super Admin",
        email="admin@soft.com",
        is_superadmin=True,
        password=sha256_crypt.hash("admin123")
    )
    db.session.add(admin)
    db.session.commit()
    return admin

def test_full_company_flow(client, superadmin):
    """
    Teste completo:
    1. Faz login do superadmin
    2. Cria uma nova empresa
    3. Lista empresas e valida se foi criada
    """

    # === 1 Login ===
    login_payload = {
        "company_name": "",
        "email": "admin@soft.com",
        "password": "admin123"
    }
    login_res = client.post("/api/auth/login", json=login_payload)
    assert login_res.status_code == 200
    tokens = login_res.get_json()
    access_token = tokens["access_token"]

    # === 2 Criação da empresa ===
    create_payload = {
        "name": "Denso Brasil",
        "cnpj": "12345678000199",
        "address": "Rua do Trabalhador 1",
        "phone": "987654321",
        "website": "densodobrasil.com",
        "logo": None,
        "email": "delei@denso.com"
    }
    create_res = client.post(
        "/api/core/companies",
        headers={"Authorization": f"Bearer {access_token}"},
        json=create_payload
    )
    assert create_res.status_code == 201
    data = create_res.get_json()
    assert "criada com sucesso" in data["message"].lower()

    # === 3️ Listagem das empresas ===
    list_res = client.get(
        "/api/core/companies",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert list_res.status_code == 200
    companies = list_res.get_json()
    assert isinstance(companies, list)
    assert any(c["name"] == "Denso Brasil" for c in companies)
