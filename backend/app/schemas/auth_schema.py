from marshmallow import Schema, fields


class LoginSchema(Schema):
    company_name = fields.String(required=True, example="Minha Empresa LTDA")
    email = fields.Email(required=True, example="admin@empresa.com")
    password = fields.String(required=True, load_only=True, example="123456")


class TokenResponseSchema(Schema):
    access_token = fields.String()
    refresh_token = fields.String()
    user = fields.Dict()
