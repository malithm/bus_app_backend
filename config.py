import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # Enable debug mode.
    DEBUG = os.getenv('APP_DEBUG')
    # Connect to the database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    # Turn off the Flask-SQLAlchemy event system and warning
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')