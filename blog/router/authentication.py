from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, model, hashing
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(model.User).filter(model.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Invalid Credentials")
    if hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Incorrect password")
    return user
