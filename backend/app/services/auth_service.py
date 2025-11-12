from flask_jwt_extended import create_access_token, create_refresh_token
from app.models.core_model import User, Company
from app import db
from passlib.hash import sha256_crypt as sha256


def authenticate_user(company_name: str, email: str, password: str):
    """
    Autentica o usuário dentro de uma empresa específica.
    """
    company = Company.query.filter_by(name=company_name).first()
    if not company:
        user = User.query.filter_by(email=email).first()
        if user and user.is_superadmin:
            company = None
        else:
            raise ValueError("Empresa não encontrada.")
    if company:
        user = User.query.filter_by(company_id=company.id, email=email).first()
    if not user or not sha256.verify(password, user.password):
        raise ValueError("Credenciais inválidas.")

    # Gera os tokens JWT
    claims = {
        "company_id": company.id if company else None,
        "is_superadmin": user.is_superadmin
    }
    
    access_token = create_access_token(identity=str(user.id), additional_claims=claims)
    refresh_token = create_refresh_token(identity=str(user.id), additional_claims=claims)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": {
            "user_id": user.id,
            "name": user.name,
            "email": user.email,
            "company_id": company.id if company else None,
            "company": company.name if company else None,
            "is_superadmin": user.is_superadmin,
            "is_admin": user.is_admin
        }
    }
