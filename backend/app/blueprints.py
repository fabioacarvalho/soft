from flask_smorest import Blueprint

core_blp = Blueprint(
    "Core",
    "core",
    url_prefix="/api/core",
    description="Endpoints principais da aplicação",
)

auth_blp = Blueprint(
    "Auth",
    "auth",
    url_prefix="/api/auth",
    description="Endpoints de autenticação JWT"
)