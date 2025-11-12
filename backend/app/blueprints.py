from flask_smorest import Blueprint

core_blp = Blueprint(
    "Core",
    __name__,
    url_prefix="/api/core",
    description="Endpoints principais da aplicação",
    # tags=["Core"]
)
