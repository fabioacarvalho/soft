from flask_smorest import abort
from flask.views import MethodView
from app.blueprints import core_blp
from app.schemas.core_schema import CompanyCreateSchema, CompanyWithAdminResponseSchema, CompanyResponseSchema
from app.utils.decorators import admin_required
from flask_jwt_extended import jwt_required
from app.services.core_service import (
    create_company_with_admin, update_company, delete_company, get_all_companies, get_company_by_id
)


@core_blp.route("/companies")
class CompanyResource(MethodView):
    """Criação de empresas e usuário administrador"""
    
    @core_blp.response(200, CompanyResponseSchema(many=True))
    @admin_required
    def get(self):
        """Endpoint para retornar as empresas cadastradas"""
        from app.models.core_model import Company
        companies = get_all_companies()
        if not companies:
            abort(404, message="Nenhuma empresa cadastrada.")
        return companies

    @core_blp.arguments(CompanyCreateSchema)
    @core_blp.response(201, CompanyWithAdminResponseSchema)
    @admin_required
    def post(self, data):
        """Cria uma nova empresa e um usuário admin padrão"""
        try:
            result = create_company_with_admin(data)
            return {
                "message": f"Empresa criada com sucesso.",
                "result": result
            }
        except Exception as e:
            abort(400, message=str(e))


@core_blp.route("/companies/<int:company_id>")
class CompanyResource(MethodView):
    """Manipulação de uma empresa específica"""

    @core_blp.response(200, CompanyResponseSchema)
    @jwt_required()
    def get(self, company_id):
        """Busca uma empresa específica"""
        company = get_company_by_id(company_id)
        if not company:
            abort(404, message="Empresa não encontrada.")
        return company

    @core_blp.arguments(CompanyCreateSchema)
    @core_blp.response(200, CompanyResponseSchema)
    @jwt_required()
    def put(self, data, company_id):
        """Atualiza uma empresa"""
        try:
            result = update_company(company_id, data)
            return {
                "message": f"Empresa '{data['name']}' atualizada com sucesso.",
                "result": result
            }
        except Exception as e:
            abort(400, message=str(e))

    @admin_required
    @core_blp.response(204)
    def delete(self, company_id):
        """Deleta uma empresa"""
        try:
            delete_company(company_id)
            return {}
        except Exception as e:
            abort(400, message=str(e))