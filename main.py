from fastapi import FastAPI, Path
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def index():
 return {"message": "Hello World"}

@app.get("/hello")
async def hello(name:str,age:int):
 return {"name": name, "age":age}

@app.get("/hi/{name}")
async def hello(name:str):
 return {"name": name}

@app.get("/hello2/{name}/{age}")
async def hello(*, name:str=Path(...,min_length=3,
max_length=10), age:int=Path(..., gt=15, lt=80)):
 return {"name": name, 'age': age}




class Student(BaseModel):
 id: int
 name: str = Field(None, title="The description of the item", max_length=10)
 subjects: List[str] = []

data = {
  'id': 1,
  'name': 'Ravikumar',
  'subjects': ["Eng", "Maths", "Sci"],
 }

s1 = Student(**data)

@app.post("/students/")
async def student_data(s1: Student):
 return s1
