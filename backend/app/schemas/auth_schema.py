from marshmallow import Schema, fields


class LoginSchema(Schema):
    company_name = fields.String(required=False, allow_none=True, example="Empresa_LTDA")  # In the future, we might use this field to identify the company, so we probably should change it to required=True
    email = fields.Email(required=True, example="admin@empresa.com")
    password = fields.String(required=True, load_only=True, example="admin123")


class TokenResponseSchema(Schema):
    access_token = fields.String()
    refresh_token = fields.String()
    user = fields.Dict()
