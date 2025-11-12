from flask_smorest import abort
from flask.views import MethodView
from app.blueprints import core_blp
from app.schemas.core_schema import CompanyCreateSchema, CompanyWithAdminResponseSchema, CompanyResponseSchema
from app.services.core_service import create_company_with_admin
from app.utils.decorators import admin_required


@core_blp.route("/companies")
class CompanyResource(MethodView):
    """Criação de empresas e usuário administrador"""
    
    @core_blp.response(200, CompanyResponseSchema(many=True))
    @admin_required
    def get(self):
        """Endpoint para retornar as empresas cadastradas"""
        from app.models.core_model import Company
        companies = Company.query.all()
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
                "message": f"Empresa '{data['name']}' criada com sucesso.",
                "result": result
            }
        except Exception as e:
            abort(400, message=str(e))
