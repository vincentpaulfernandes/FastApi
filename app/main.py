from typing import Optional,List
from fastapi import Body, FastAPI,Response,status,HTTPException,Depends,APIRouter
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils

from .database import engine,get_db
from sqlalchemy.orm import Session

from .routers import post, user,auth


models.Base.metadata.create_all(bind=engine)



app=FastAPI()






while True:

    try:
        conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='12345678',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("database connection was successfull")
        break
    except Exception as error:
        print("connecting to database has failed")
        print("error",error)
        time.sleep(2)



my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},
          {"title":"fav food","content":"i like pizza","id":2}]


def find_post(id):
    for p in my_posts:
        if p['id']== id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id']==id:
            return i



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)



@app.get("/")
async def root():
    return {"message": "welcome to my vincent"} 







