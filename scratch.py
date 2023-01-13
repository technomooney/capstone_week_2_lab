import random
from dataclasses import dataclass

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)


@dataclass
class StudentData:
    name: str
    school_id:str
    gpa:float

def __str__(self) -> str:
    string_output = f"""Student Name: {self.name}
        ID: {self.school_id}
        Grade Point Average: {self.gpa}"""
    return string_output


class Student:
    def __init__(self, name, school_id, gpa) -> None:
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self) -> str:
        string_output = f"""Student Name: {self.name}
    ID: {self.school_id}
    Grade Point Average: {self.gpa}"""
        return string_output

class Author:
    def __init__(self,name) -> None:
        self.name = name
        self.published_books = []

    def publish(self,title_name):
        self.published_books.append(title_name.title())
    
    def __str__(self) -> str:
        author_string =f"{self.name.title()} has the following books published: \n"
        if self.published_books:
            for item_number,book_name in enumerate(self.published_books):
                author_string+=f"\tBook {item_number+1}: {book_name}\n"
        else:
            author_string+="No Books Published yet."
        return author_string