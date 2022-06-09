from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    colg: str
    age: int

class UpdateStudent(BaseModel):
    name: Optional[str] = None 
    colg: Optional[str] = None
    age: Optional[int] = None

students = {
    1 : {
        "name" : "Achintya",
        "colg"  : "Amity",
        'age' : 21
    },
    2 : {
        "name" : "Pranshu",
        "colg"  : "Echelon",
        'age' : 19
    }
}

# basic msg display
@app.get("/")
def index():
    return {'msg' : 'Hello Achintya'}

# getting info of students using id
@app.get('/info/{id}')
def get_info(id: int = Path(None, description='Enter Id of the student', gt=0, lt=10)):
    if id in students.keys():
        return students[id]
    else:
        return {'Error' : 'Id not in list'} 

# displaying all the info
@app.get("/all")
def get_all():
    new_dict = {}
    return students

    return new_dict

# gets the length of list
@app.get('/len')
def get_len():
    return {'Length' : len(students)}

# getting info using name
@app.get('/get_by_name')
def get_students(name: str = None):
    for id in students:
        if students[id]['name'] == name:
            return students[id]
    return {'Data' : 'No Students Found'} 

# adding a new student
@app.post("/create/{id}")
def create_student(id: int, student: Student):
    if id in students:
        return {'Error' : 'Student Exists'}
    else:
        students[id] = student
        return students[id]

# updating a student using id
@app.put('/update/{id}')
def update_student(id: int, newStudent: UpdateStudent):
    if id not in students:
        return {'Error' : 'Id not in Students'}

    if newStudent.name != None:
        students[id].name = newStudent.name 

    if newStudent.age != None:
        students[id].age = newStudent.age 

    if newStudent.colg != None:
        students[id].colg = newStudent.colg 
        
    return students[id]

@app.delete('/delete/{id}')
def delete_student(id: int):
    if id not in students:
        return {'Error': 'Student not in Database'}
    
    del students[id]
    return {f'msg': 'Student deleted successfully'}
