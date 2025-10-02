from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app.forms import LoginForm
from app.models import User

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

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Usuárop ou senha inválidos", "danger")
            return redirect(url_for('main.login'))
        else:
            login_user(user, remember=form.remember_me.data)
            flash('Login efetuado com sucesso!', 'success')
            return redirect(url_for('main.index'))

    return render_template("login.html", title='Entrar', form=form)
