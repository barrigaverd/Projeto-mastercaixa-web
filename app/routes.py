from flask import Blueprint

# Cria um Blueprint chamado 'main'. Blueprints são como
# um conjunto de rotas que podem ser registradas na aplicação.
bp = Blueprint('main', __name__)

# Esta é a nossa primeira "view function" ou rota.
# O decorador @bp.route('/') diz ao Flask para chamar
# esta função quando alguém acessar a URL raiz ('/').
@bp.route('/')
@bp.route('/index')
def index():
    return "<h1>Olá, Mundo! O Projeto MasterCaixa-Web está no ar!</h1>"