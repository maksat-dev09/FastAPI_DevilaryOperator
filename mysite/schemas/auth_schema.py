from pydantic import BaseModel, EmailStr
from datetime import date

class UserRegisterSchema(BaseModel):
    username: str
    email: EmailStr
    phone_number: str
    password: str

class UserLoginSchema(BaseModel):
    username: str
    password: str

class UserUpdateSchema(BaseModel):
    username: str
    email: EmailStr
    phone_number: str

class UserOutputSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    phone_number: str
    registered_date: date

