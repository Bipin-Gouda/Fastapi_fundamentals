from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import List
import schemas 
import models   # from models we will import the blog table
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from hashing import Hash


app = FastAPI()

models.Base.metadata.create_all(engine)     # creates/loads all the models/ORMtables into the db

def get_db():                     # # Session is not a pydantic type so error therefore we use Depends from FastAPi which converts it to a Pydantic type and create a function to access the seeion and db
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog',status_code=status.HTTP_201_CREATED, tags=['blogs'])     # we can find the recommended status codes list
def create(request: schemas.Blog, db: Session = Depends(get_db)):   # request is obj of Blog class importd from schemas we enter/get its values from the browser (client)
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)               # client gave details using docs (kind of a form only)
    db.add(new_blog)                          # we return the pydantic req response to docs to test it , we can send it to DB as well 
    db.commit()                          
    db.refresh(new_blog)
    return new_blog


@app.get('/blog', response_model = List[schemas.ShowBlog], tags=['blogs'])  # as multiple values here, we need a list
def allblogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=200, response_model = schemas.ShowBlog, tags=['blogs'])
def show(id, response: Response, db: Session = Depends(get_db)):       # 'response' is a 'Response' class type object (Fastapi, Pydantic)
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f"Blog with the id {id} is not available"}
    return blog

# Causing Error (Solved)
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):  # we define request b/c we need data in this format as defined in schemas Blog
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"This id was not found")
    blog.update(request.dict())
    db.commit()
    return {"Message":f"Updated the blog with id {id}"}


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"This id was not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"Message":f"Deleted the blog with id {id}"}



@app.post('/user', response_model = schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password) )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}', response_model = schemas.ShowUser, tags=['users'])
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"User with the id {id} is not available")
    return user





""" NOTE: so basically request:schemas.Blog here is the format in which I recieve data from the user 
and models.Blog is the format in which the data is stored in DB."""