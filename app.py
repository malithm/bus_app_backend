# ----factory method class initialization-----
from app import create_app
app = create_app()

from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# -----importmodels-----
# from app.models.base_model import BaseModel
# from app.models.user_model import UserModel

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

# ----initialize db----------
# db = SQLAlchemy(app, model_class=BaseModel)
db = SQLAlchemy(app)
ma = Marshmallow(app)

class UserModel(db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String(120))
    address = Column(String(120))
    email = Column(String(100))
    
    def __init__(self, id, name, age, address, email):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.email = email

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        
user_schema = UserSchema()
users_schema = UserSchema(many=True)

def index():
    return "Welcome to API"

def test():
    return "Test is working"

# from app.controllers.user_controller import index

"""
user_bp = Blueprint('user_bp', __name__, url_prefix='/app')
app.register_blueprint(user_bp)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/test/', methods=['GET'])(test)

"""

if __name__ == "__main__":
    app.run()
