from scratch import *

test_student = Student("Bob Saggit","AS2415GD",3.75)
print(test_student)
test_student.gpa = 4.0
print(test_student)


shakespeare = Author("William Shakespeare")
shakespeare.publish("Hamlet")
shakespeare.publish("The Comedy of Errors")

print(shakespeare)

test_student_dataclass = Student("John Smith","GE9722AT",1.75)
print(test_student_dataclass)
test_student_dataclass.gpa =2.0
print(test_student_dataclass)