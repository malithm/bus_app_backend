from . import *
from app.models.user_model import UserModel
from app.schemas.user_schema import UserSchema
from app.extensions import db

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def index():
    return "Welcome to API"

def store():
    print("route....", request)
    name = request.json.get("name", "")
    email = request.json.get("email", "")
    user = UserModel(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)

def all():
    users = UserModel.query.all()
    print("users = ", users)
    return jsonify(users_schema.dump(users))

def show(user_id):
    print("user_id = ", user_id)
    user = UserModel.query.get(user_id)
    return user_schema.jsonify(user)

def update(user_id):
    name = request.json.get("name", "")
    email = request.json.get("email", "")
    user = UserModel.query.get(user_id)
    user.name = name
    user.email = email
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)

def delete(user_id):
    user = UserModel.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)