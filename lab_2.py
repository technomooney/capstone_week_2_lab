from dataclasses import dataclass
class Author:
    def __init__(self,name) -> None:
        self.name = name
        self.published_books = []

    def publish(self,title_name):
        if title_name.title() in self.published_books:
            raise ValueError(f"{title_name} has already been published. ")
        else:
            self.published_books.append(title_name.title())
    
    def __str__(self) -> str:
        author_string =f"{self.name.title()} has the following books published: \n"
        if self.published_books:
            for item_number,book_name in enumerate(self.published_books):
                author_string+=f"\tBook {item_number+1}: {book_name}\n"
        else:
            author_string+="No Books Published yet."
        return author_string


@dataclass
class StudentData:
    # data classes dont need any __init__ funtions. things are auto gernerated. 
    name: str
    school_id: str
    gpa: float

    def __str__(self) -> str:  # creating a customised string output.
        string_output = f"""Student Name: {self.name}
            ID: {self.school_id}
            Grade Point Average: {self.gpa}"""
        return string_output


def main():
    shakespeare = Author("William Shakespeare")
    shakespeare.publish("Hamlet")
    shakespeare.publish("The Comedy of Errors")

    print(shakespeare)

    test_student = StudentData("Bob Saggit","AS2415GD",3.75)
    print(test_student)
    test_student.gpa = 4.0
    print(test_student)
    shakespeare.publish("Hamlet")

main()
