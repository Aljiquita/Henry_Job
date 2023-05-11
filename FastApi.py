import pandas as pd
import datetime as dt
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from uuid import uuid4 as uui




app = FastAPI()
# Levantar el servidor
# uvicorn FastApi:app --reload

posts = []


# Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now() # la fecha actual
    published_at: Optional[datetime] 
    published: bool = False


@app.get('/')
def read_root():
    return {"welcome": "Hola ALJIQUITA"}

@app.get("/posts")
def get_posts():
    return posts

@app.post("/posts")
def save_post(post: Post):
    post.id = str(uui()) 
    posts.append(post.dict())
    print()
    print(posts)
    return posts[-1]


# buscar un id de la lista
@app.get("/posts/{post_id}")
def get_post(post_id: str):
    print(post_id)
    for post in posts:
        if post['id'] == post_id:
            return post
    return HTTPException( status_code=404, detail= 'Post Not found' )

# Quitar u id de la lista
@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
        return {"message": "La publicacion se ha eliminado"}
    return "No se encontró"

#  https://www.youtube.com/watch?v=_eWEmRWhk9A&t=2726s&ab_channel=FaztCode
# time 45:28