from app import db
from app.models.core_model import Company, User


def create_company_with_admin(data):
    company = Company(
        name=data["name"],
        cnpj=data["cnpj"],
        email=data.get("email"),
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
        email=data.get("email") or f"admin{company.id}@soft.com",
        is_admin=True
    )
    admin_user.set_password(company.cnpj)
    db.session.add(admin_user)
    db.session.commit()

    return {"company_id": company.id, "admin_id": admin_user.id}

def get_all_companies():
    return Company.query.all()

def get_company_by_id(company_id):
    return Company.query.get(company_id)

def update_company(company_id, data):
    company = Company.query.get(company_id)
    if not company:
        return None

    company.name = data.get("name", company.name)
    company.cnpj = data.get("cnpj", company.cnpj)
    company.address = data.get("address", company.address)
    company.phone = data.get("phone", company.phone)
    company.website = data.get("website", company.website)
    company.logo = data.get("logo", company.logo)

    db.session.commit()
    return company

def delete_company(company_id):
    company = Company.query.get(company_id)
    if not company:
        return False

    db.session.delete(company)
    db.session.commit()
    return True