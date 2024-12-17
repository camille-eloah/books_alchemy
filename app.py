from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from controllers.auth_bp import auth_bp
from controllers.books_bp import books_bp

# Inicialização das extensões
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

# Configuração da aplicação
app = Flask(__name__)
app.config.from_object(Config)

# Inicialização das extensões
db.init_app(app)
login_manager.init_app(app)

# Registro dos Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(books_bp, url_prefix='/books')

# Modelo de Usuário necessário para o Flask-Login
from models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rota principal
@app.route('/')
def index():
    return 'Bem-vindo ao Sistema de Reserva de Livros! Acesse /auth/login para começar.'

# Execução do servidor
if __name__ == '__main__':
    app.run(debug=True)
