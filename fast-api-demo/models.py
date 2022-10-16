from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    _id : str
    name : str
    password : str
    description: str = None

class SchoolLocation(BaseModel):
    country : str
    country_subidivision: str = None
    locality: str = None

class StudentProfile(BaseModel):
    gender: int # 0: male, 1: female, 2: other
    age: int
