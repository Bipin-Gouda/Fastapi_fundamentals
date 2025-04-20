from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()   #instance

@app.get('/')      # path | route | endpoint (samething) 
def index():
    return {'data':{'name':'Bipin'}}  # try to return in json format in APIs instead of strings


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog')              # using Query Parameters for the task (if providing default value, will have to provide for all query parameters)
def queryparam(limit=10, published:bool = True, sort: Optional[str]=None):
    #return published
    if published:
        return {'data':f'{limit} published blogs from the DB'}
    else:
        return {'data':f'{limit} blogs from the DB'}

@app.get('/blog/{id}')         # creating route with Path Parameter. Function Kept below '/blog/unpublished'
def show(id: int):
    # fetch blog with id = id
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id 
    return {'data':{'comments blog ':{'comment 1','comment 2'}}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/create')                #using Pydantic model to define schema for Post request
def create_blog(blog: Blog):     # request is simply a variable name here
    return {'data':f"blog created with title: {blog.title} and body: {blog.body} and published status as {blog.published}"}

# we define the request body structure in our API and recieve the request body from the Frontend/browser
