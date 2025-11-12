from pydantic import BaseModel

class Student(BaseModel):

    name: str = 'nitish'

new_student = {}

student = Student(**new_student)
print(type(student))
print(student.name)