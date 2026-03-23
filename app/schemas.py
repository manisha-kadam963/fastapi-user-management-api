from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str
    age: int
    email: str
    password: str = Field(..., max_length=72)

class UserLogin(BaseModel):  
    email: str
    password: str = Field(..., max_length=72)
