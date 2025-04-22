from pydantic import BaseModel
from typing import List

# Note: We call the Pydantic Models as Schemas and SQL Alchemy models as Models
# We use these schemas to recieve/display/structure the data in a specific format

# Blog recieving model
class Blog(BaseModel):
    title:str
    body:str
    class Config():                 
         from_attributes = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blog]       # we want the blogs to be displayed in Blog format, we dont use ShowBlog as it will cause issue
    class Config():                 
         from_attributes = True

# response_model
class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser                 # creator is of type ShowUser
    class Config():                  # needed in case we dont return a dictionary and are using response_model, using db.query()
        from_attributes = True
  
class Login(BaseModel):
    username: str
    password: str


# models for JWT

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None     # refers to email