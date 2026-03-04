# main file jaha pehle data import, phir func from utils, then io..
import json
from utils import load_students, get_top_students, avg_mrks  #func name

with open("students.json", "r") as file:
    data = json.load(file)

students = load_students(data)
top_students = get_top_students(students)
avg_std = avg_mrks(students)

for std in top_students:
    print(std.name, std.marks)

for a in avg_std:
    print ("Avg ", a.name, a.marks)


