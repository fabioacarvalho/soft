from app import db
from passlib.hash import pbkdf2_sha256 as sha256


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    website = db.Column(db.String(100))
    logo = db.Column(db.String(255))

    users = db.relationship("User", backref="company", cascade="all, delete-orphan")

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
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(100))
    bio = db.Column(db.Text)
    avatar_url = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password: str):
        from passlib.hash import sha256_crypt
        self.password = sha256_crypt.hash(password)

    def check_password(self, password: str):
        from passlib.hash import sha256_crypt
        return sha256_crypt.verify(password, self.password)
