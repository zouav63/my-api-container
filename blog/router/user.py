from blog import main
from fastapi import APIRouter, Depends, status
from .. import schemas, database, model, hashing
from sqlalchemy.orm import Session

router=APIRouter(
    prefix='/user',
    tags=['users']
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user=model.User(email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(database.get_db)):
    return db.query(model.User).filter(model.User.id==id).first()