from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Nome de Usuário", validators=[DataRequired("Este campo é requerido")])
    password = PasswordField('Senha', validators=[DataRequired("Este campo é requerido")])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired("Este campo é requerido")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired("Este campo é requerido")])
    password2 = PasswordField("Confirmar Senha", validators=[DataRequired("Este campo é requerido"),EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()
        
        # 3. Se 'user' não for None, significa que encontrou um usuário.
        if user is not None:
            # 4. Lança um erro de validação. A mensagem será mostrada ao usuário.
            raise ValidationError('Este nome de usuário já está em uso. Por favor, escolha outro.')
        
    def validate_email(self, email):
   
        user = User.query.filter_by(email=email.data).first()
        
        # 3. Se 'user' não for None, significa que encontrou um usuário.
        if user is not None:
            # 4. Lança um erro de validação. A mensagem será mostrada ao usuário.
            raise ValidationError('Este email já está em uso. Por favor, escolha outro.')