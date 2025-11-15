from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, get_jwt
from app.schemas.auth_schema import LoginSchema, TokenResponseSchema
from app.services.auth_service import authenticate_user
from app.blueprints import auth_blp
from app.models.core_model import User
from app.utils.permissions import ROLE_PERMISSIONS


@auth_blp.route("/login")
class LoginResource(MethodView):
    @auth_blp.arguments(LoginSchema)
    @auth_blp.response(200, TokenResponseSchema)
    def post(self, credentials):
        try:
            return authenticate_user(**credentials)
        except ValueError as e:
            abort(401, message=str(e))


@auth_blp.route("/refresh")
class TokenRefreshResource(MethodView):
    @jwt_required(refresh=True)
    @auth_blp.response(200, TokenResponseSchema)
    def post(self):
        """
        Gera novo access token a partir do refresh token.
        """
        identity = get_jwt_identity()
        new_access_token = create_access_token(identity=identity)
        new_refresh_token = create_refresh_token(identity=identity)

        return {
            "access_token": new_access_token,
            "refresh_token": new_refresh_token,
            "user": identity
        }


@auth_blp.route("/me")
class ProfileResource(MethodView):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()
        claims = get_jwt()

        return {
            "logged_user": identity,
            "company_id": claims.get("company_id"),
            "is_superadmin": claims.get("is_superadmin")
        }


@auth_blp.route("/me/permissions")
class MePermissionsResource(MethodView):

    @jwt_required()
    def get(self):
        user = User.get_current()

        return {
            "role": user.role,
            "permissions": list(ROLE_PERMISSIONS.get(user.role, []))
        }
