from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from app.models import User
from flask_login import login_manager

db = SQLAlchemy()
migrate = Migrate()
login = login_manager()

def create_app(config_class=Config):
    # Cria a instância da aplicação Flask
    app = Flask(__name__)
    
    # Carrega as configurações a partir da classe Config
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'main.login'

    # --- Registro de Blueprints ---
    # Blueprints ajudam a organizar as rotas.
    # Vamos registrar nosso blueprint principal aqui.
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Retorna a instância da aplicação configurada
    return app

@login.user_loader
def loginuser(id):
    usuario = User.query.get(int(id))

from app import models