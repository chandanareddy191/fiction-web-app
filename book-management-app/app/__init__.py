from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from flask import Flask
from flask import send_from_directory, render_template_string
import os

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per day", "30 per hour"]
)

def create_app():
    
    
    app = Flask(__name__)
    
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
    app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'
    
    
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    limiter.init_app(app)
    
    
    @app.route('/')
    
    def home():
        return jsonify({
            "endpoints": {
                "auth": {
                    "login": "/api/auth/login",
                    "profile": "/api/auth/profile",
                    "register": "/api/auth/register"
                },
                "books": {
                    "create": "/api/books",
                    "delete": "/api/books/<id>",
                    "get_all": "/api/books",
                    "get_one": "/api/books/<id>",
                    "update": "/api/books/<id>"
                }
            },
            "message": "Welcome to Book Management API"
        })
    
    return app