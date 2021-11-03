from passlib.context import CryptContext 
pwd_ctx=CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_ctx.hash(password)

    def verify(hashed_password, password):
        return pwd_ctx.verify(password, hashed_password)