# This file creates class, object and constructor 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_topper(self):
        return self.marks > 90
    
    def is_avg(self):
        return self.marks > 60 and self.marks < 80