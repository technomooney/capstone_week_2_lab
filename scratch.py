import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)


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

    