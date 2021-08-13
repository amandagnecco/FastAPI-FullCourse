from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()



@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    # returns only 10 published blogs by default
    if published:
        return {'data' : f'{limit} published blogs from db'}
    else:
        return {'data' : f'{limit} blogs from db'}



@app.get('/blog/umpublished')
def unpublished():
    return {'data': 'all umpublished blogs'}



@app.get('/blog/{id}')
def show(id: int):
    return {'data' : id}



@app.get('/blog/{id}/comments')
def comments(id, limit = 10):
    return {'data' : {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



@app.post('/blog')
def create_blog(request: Blog):
    return{'data': f'Blog is created as: {request.title}'}