# models/tables for the db using ORM we create so we use class and obj to create tables
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

# Creating Blog model/table
class Blog(Base):                                          # Never recommended to use a once deleted PK (id)
    __tablename__ = 'blogs'                                # Autoincrementing PK, starts with 1 but we can change the seq to start from anywhere as per requirement
    id = Column(Integer, primary_key = True, index = True)  # SQLAlchemy and most relational databases (like SQLite) use a feature called auto-incrementing primary keys.
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    creator = relationship("User", back_populates="blogs")


# Currently the User and Blog table have no links the ids are also different unrelated columns (creator added later)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")