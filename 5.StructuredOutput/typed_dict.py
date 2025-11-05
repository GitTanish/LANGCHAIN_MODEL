from typing import TypedDict

class Person(TypedDict):
    name:str
    age: int

new_person: Person ={'name':'shinji', 'age':14}

print(new_person)