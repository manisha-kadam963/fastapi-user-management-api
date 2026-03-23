from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal
from app.auth import hash_password, verify_password, create_token

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# REGISTER
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = hash_password(user.password)
    
    new_user = models.User(
        name=user.name,
        age=user.age,
        email=user.email,
        password=hashed
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created"}

# LOGIN
@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not db_user:
        return {"error": "User not found"}

    if not verify_password(user.password, db_user.password):
        return {"error": "Wrong password"}

    token = create_token({"email": db_user.email})

    return {"access_token": token}