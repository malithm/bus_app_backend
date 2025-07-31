from . import *
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase

class BaseModel(DeclarativeBase):
    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(String)