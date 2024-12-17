from app import create_app
from db import db

app = create_app()

with app.app_context():
    db.create_all() 
    print("Tabelas criadas com sucesso!")