from marshmallow import Schema, fields, validate, validates, ValidationError
import re


# -------------------------- Funções auxiliares de validação -------------------------------
def validar_cnpj(cnpj: str):
    """Valida CNPJ básico (somente formato e tamanho)"""
    cnpj = re.sub(r'\D', '', cnpj or '')
    if len(cnpj) != 14:
        raise ValidationError("CNPJ inválido — deve conter 14 dígitos.")
    return cnpj


# -------------------------- Company Schemas -------------------------------
class CompanyCreateSchema(Schema):
    """Schema para criação de uma nova empresa"""
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    cnpj = fields.Str(required=True, validate=validar_cnpj)
    address = fields.Str(validate=validate.Length(max=255))
    phone = fields.Str(validate=validate.Length(max=20))
    website = fields.Str(validate=validate.Length(max=100))
    logo = fields.Str(validate=validate.Length(max=255))
    email = fields.Email(
        required=False,
        metadata={"description": "E-mail do usuário admin (opcional)"}
    )


class CompanyResponseSchema(Schema):
    """Schema de retorno da empresa"""
    id = fields.Int(dump_only=True)
    name = fields.Str()
    cnpj = fields.Str()
    address = fields.Str()
    phone = fields.Str()
    website = fields.Str()
    logo = fields.Str()
    users = fields.List(fields.Int())


# -------------------------- User Schemas -------------------------------
class UserBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    email = fields.Email()
    title = fields.Str()
    bio = fields.Str()
    avatar_url = fields.Str()
    is_admin = fields.Bool()


class UserResponseSchema(UserBaseSchema):
    """Schema para resposta de usuário"""
    company_id = fields.Int()


class CompanyWithAdminResponseSchema(Schema):
    """Retorno após criação de uma empresa com usuário admin"""
    company_id = fields.Int()
    admin_id = fields.Int()
