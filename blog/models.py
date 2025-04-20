# models/tables for the db using ORM we create so we use class and obj to create tables
from sqlalchemy import Column, Integer, String
from database import Base

# Creating Blog model/table
class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key = True, index =True)
    title = Column(String)
    body = Column(String)