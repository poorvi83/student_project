# from models k reference, make functions here.
from models import Student    #module import

def load_students(data):
    students = []   #list to store Student obj
    for item in data:
        std = Student(item["name"], item["marks"])
        students.append(std)
    return students 

def get_top_students(students):    
    toppers = []    
    for student in students:
        if student.is_topper():
            toppers.append(student)    
    return toppers

def avg_mrks(students):
    avg = []
    for i in students:
        if i.is_avg():
            avg.append(i)
    return avg

