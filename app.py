from flask import Flask, render_template
from controllers.auth_bp import auth_bp
from controllers.books_bp import books_bp
from db import db, login_manager, Config
from models.user import User 

login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(books_bp, url_prefix='/books')

    @app.route('/')
    def index():
        return render_template('index.html')  
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
