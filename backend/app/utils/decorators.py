from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask_smorest import abort


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if not claims.get("is_superadmin"):
            abort(403, message="Acesso restrito ao administrador geral.")
        return fn(*args, **kwargs)
    return wrapper
