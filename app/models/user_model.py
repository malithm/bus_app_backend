from . import *
from app.extensions import db

class UserModel(db.Model):
    __tablename__ = 'user'
    
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
        