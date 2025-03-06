import os
from datetime import timedelta

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-very-secret-key-change-in-production')
    
   
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    
    
    RATELIMIT_DEFAULT = "100 per day"
    RATELIMIT_STORAGE_URL = "memory://"

  
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')