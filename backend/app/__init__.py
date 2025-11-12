from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os
from app.blueprints import core_blp

# Extensões
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = JWTManager()
api = Api()
cors = CORS()


def create_app():
    app = Flask(__name__)

    # Configurações do ambiente
    app.config.from_object(os.getenv("FLASK_ENV", "config.DevelopmentConfig"))

    cors.init_app(app, origins=["http://localhost:3000"], supports_credentials=True)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)
    api.init_app(app)

    # Registrar Blueprints
    api.register_blueprint(core_blp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)