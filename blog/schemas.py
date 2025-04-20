from pydantic import BaseModel

# Note: We call the Pydantic Models as Schemas and SQL Alchemy models as Models

class Blog(BaseModel):
    title:str
    body:str


# response_model
class ShowBlog(BaseModel):
    title:str
    body:str
    class Config():                  # needed in case we dont return a dictionary and are using response_model, using db.query()
        from_attributes = True


class User(BaseModel):
    name:str
    email:str
    password:str