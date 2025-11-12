from app import db
from app.models.core_model import Company, User


def create_company_with_admin(data):
    company = Company(
        name=data["name"],
        cnpj=data["cnpj"],
        address=data.get("address"),
        phone=data.get("phone"),
        website=data.get("website"),
        logo=data.get("logo")
    )
    db.session.add(company)
    db.session.flush()  # gera company.id

    admin_user = User(
        company_id=company.id,
        name=f"{company.name} Admin",
        email=data.get("email") or f"admin@{company.name.lower().replace(' ', '')}.com",
        is_admin=True
    )
    admin_user.set_password(company.cnpj)
    db.session.add(admin_user)
    db.session.commit()

    return {"company_id": company.id, "admin_id": admin_user.id}
