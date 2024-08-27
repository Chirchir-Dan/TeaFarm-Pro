from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mysq1server%40@localhost/teafarm'
    
    db.init_app(app)

    with app.app_context():
        from app import models # Import models to register them with SQLAlchemy
        from app import routes
    return app
