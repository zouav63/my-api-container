from fastapi import FastAPI, Depends, status, HTTPException
from . import model
from .database import engine 
from .router import blog,user,authentication

model.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)