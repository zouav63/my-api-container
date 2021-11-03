from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, model
from sqlalchemy.orm import Session

router=APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get('/')
def get_all(db: Session = Depends(database.get_db)):
    blogs= db.query(model.Blog).all()
    return blogs

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(blog: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog=model.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db: Session = Depends(database.get_db)):
    db.query(model.Blog).filter(model.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return "done"

@router.put('/{id}')
def update(id:int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog=db.query(model.Blog).filter(model.Blog.id==id)
    blog.update({'title':request.title, 'body':request.body})
    db.commit()
    return 'done'

@router.get('/{id}')
def get_blog(id:int, db: Session = Depends(database.get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog...")
    return blog
