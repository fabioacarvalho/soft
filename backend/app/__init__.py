from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os
from app.blueprints import core_blp, auth_blp


# Extensões
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = JWTManager()
api = Api()
cors = CORS()


def create_app(config_class=None):
    app = Flask(__name__)

    # Setup environment configuration
    # app.config.from_object(os.getenv("FLASK_ENV", "config.DevelopmentConfig"))

    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_object(os.getenv("FLASK_ENV", "config.DevelopmentConfig"))

    cors.init_app(app, origins=["http://localhost:3000"], supports_credentials=True)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)
    api.init_app(app)

    # Setup of Flask-Smorest
    api.spec.options.update(app.config.get("OPENAPI_SPEC_OPTIONS", {}))

    # Set views
    from app.views import core_view, auth_view  # noqa: F401

    # Set Blueprints
    api.register_blueprint(core_blp)
    api.register_blueprint(auth_blp)

    # Create superadmin user if not exists
    # with app.app_context():
    #     from app.models.core_model import User  # only to create superadmin if not exists
    #     User.create_superadmin_if_not_exists()

    # Flask CLI commands
    from app.utils.commands import create_superadmin
    app.cli.add_command(create_superadmin)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)