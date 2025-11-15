from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt, jwt_required
from flask_smorest import abort
from flask import jsonify
from app.models.core_model import User


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if not claims.get("is_superadmin"):
            abort(403, message="Acesso restrito ao administrador geral.")
        return fn(*args, **kwargs)
    return wrapper


def require_permission(*permissions):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            user = User.get_current()

            for perm in permissions:
                if user.has_permission(perm):
                    return fn(*args, **kwargs)

            return jsonify({"error": "permission_denied"}), 403

        return wrapper
    return decorator
