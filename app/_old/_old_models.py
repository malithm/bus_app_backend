class Base(DeclarativeBase):
    created_at = db.Column(db.String(100))
    created_by = db.Column(db.String(200))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100))

    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
