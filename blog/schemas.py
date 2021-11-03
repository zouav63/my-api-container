from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class User(BaseModel):
    email:str
    password:str

class ShowUser(BaseModel):
    email:str
    class Config():
        orm_mode=True
        
class Login(BaseModel):
    username:str
    password:str