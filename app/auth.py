from passlib.context import CryptContext
from jose import jwt

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password[:72])   # ✅ truncate

def verify_password(plain, hashed):
    return pwd_context.verify(plain[:72], hashed)   # ✅ truncate

def create_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])