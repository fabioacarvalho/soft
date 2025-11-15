import pytest
from app import create_app, db
from app.models.core_model import User, Company
from passlib.hash import sha256_crypt


@pytest.fixture
def app():
    app = create_app("config.TestingConfig")  # precisa existir no config.py
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def superadmin(app):
    existing = User.query.filter_by(email="admin@soft.com").first()
    if existing:
        return existing

    admin = User(
        name="Super Admin",
        email="admin@soft.com",
        is_superadmin=True,
        password=sha256_crypt.hash("admin123"),
        role="superadmin"
    )
    db.session.add(admin)
    db.session.commit()
    return admin


@pytest.fixture
def seller(app):
    u = User(
        company_name="",
        name="Vendedor",
        email="seller@test.com",
        role="seller"
    )
    u.set_password("seller123")
    db.session.add(u)
    db.session.commit()
    return u