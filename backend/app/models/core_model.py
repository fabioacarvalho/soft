from app import db
from passlib.hash import sha256_crypt as sha256


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    website = db.Column(db.String(100))
    logo = db.Column(db.String(255))

    users = db.relationship("User", back_populates="company", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Company {self.id} - {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cnpj": self.cnpj,
            "address": self.address,
            "phone": self.phone,
            "website": self.website,
            "logo": self.logo,
            "users": [u.id for u in self.users],
        }


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(100))
    bio = db.Column(db.Text)
    avatar_url = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)
    is_superadmin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=True)
    company = db.relationship("Company", back_populates="users")

    def __repr__(self):
        return f"<User {self.id} - {self.email}>"

    def set_password(self, password: str):
        self.password = sha256.hash(password)

    def check_password(self, password: str):
        return sha256.verify(password, self.password)
    
    @classmethod
    def create_superadmin_if_not_exists(cls):
        admin_email = "admin@soft.com"
        admin = cls.query.filter_by(email=admin_email).first()
        if not admin:
            admin = cls(
                email=admin_email,
                name="Administrador Geral",
                is_superadmin=True,
                password=sha256.hash("admin123"),
            )
            db.session.add(admin)
            db.session.commit()
            print("Superadmin criado:", admin_email)
