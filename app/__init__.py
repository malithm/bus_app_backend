from flask import Flask
from config import Config

def create_app(config_class=Config):    

    app = Flask(__name__)
    app.config.from_object(config_class)

    #initialize flask extensions
    from app.extensions import db
    db.init_app(app) 
    
    #initialize blueprints
    from app.routes.user_bp import user_bp
    app.register_blueprint(user_bp)


    return app
