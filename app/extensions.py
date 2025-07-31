from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

# app, model_class=BaseModel
# db.init_app(app)
# migrate = Migrate(app, db)