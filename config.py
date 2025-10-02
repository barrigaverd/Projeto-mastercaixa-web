import os

# Define o caminho base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Classe de configuração base. Contém configurações que são
    comuns a todos os ambientes (desenvolvimento, produção, etc.).
    """
    # Chave secreta para proteger a aplicação contra ataques (CSRF).
    # É muito importante que esta chave seja secreta em produção.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'voce-nunca-vai-adivinhar'

    # Configuração do banco de dados SQLAlchemy.
    # Define o caminho para o arquivo do nosso banco de dados.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # Desativa uma funcionalidade do SQLAlchemy que não usaremos
    # e que emite avisos se não for desativada.
    SQLALCHEMY_TRACK_MODIFICATIONS = False