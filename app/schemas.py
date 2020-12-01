from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class LibrarySchema(BaseModel):
    bookname: str = Field(...)
    subject: str = Field(...)
    authorname: str = Field(...)
    cost: float = Field(...)
    username:str
    contact_no:int
    email:EmailStr
    status:str


    class Config:
        schema_extra = {
            "example": {
                "bookname": "Programming and Data Structures",
                "subject":"Computer Science",
                "authorname": "Mark Allen Weiss",
                "cost": 399,
                "username": "Null",
                "contact_no": 0,
                "email":"null@gmail.com",
                "status":"Null"
            }
        }


class UpdateLibraryModel(BaseModel):
    username:str
    contact_no:int
    email:EmailStr
    status:str

    class Config:
        schema_extra = {
            "example": {
                "bookname": "Programming and Data Structures",
                 "subject":"Computer Science",
                "authorname": "Mark Allen Weiss",
                "cost": 399,
                "username": "John Adam",
                "contact_no": 6378392620,
                "email":"johnadam@gmail.com",
                "status":"reserved"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error, 
        "code": code, 
        "message": message
        }