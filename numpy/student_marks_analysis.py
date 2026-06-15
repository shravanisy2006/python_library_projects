"""
Student Marks Analyzer using NumPy

Features:
- Calculate student averages
- Calculate subject averages
- Find topper
- Find highest scoring subject
- Count students scoring above 75%
"""

#importing libraries
import numpy as np

#assumed data
marks = np.array([
    [1, 85, 78, 90],   # Student 1   
    [2, 72, 88, 80],   # Student 2   
    [3, 95, 91, 89],   # Student 3   
    [4, 60, 70, 65]    # Student 4
])

students = ["Alice" , "Roy" , "Mark" , "Jacob"]
subject = ["Maths" , "English" , "Science"]

#average marks of students
average_student = np.mean(marks[:,1:] , axis = 1)
mean_student = np.round(average_student, 2)
print("=== Average marks of each student:===\n ")
for student, avg in zip(students, mean_student):
    print(student ,":", avg)

#average marks per subject
average_subject = np.mean(marks[:,1:] , axis = 0)
mean_subject = np.round(average_subject, 2)
print("=== Average marks per subject:===\n")
for sub, avg in zip(subject, mean_subject):
    print(sub, ":" ,avg)

#highest marks of student
total = np.sum(marks[:,1:] , axis = 1)
highest_marks = np.argmax(total)
print("=== Highest Marks of student:===\n",(students[highest_marks])," with ",(total[highest_marks])," marks")

#highest marks per subject
total = np.sum(marks[:,1:] , axis = 0)
highest_marks = np.argmax(total)
print("=== Highest marks in subject:===\n",(subject[highest_marks]), " with ",(total[highest_marks])," marks")

#students above 75 
toppers = np.sum(average_student > 75)
print("=== Students above 75% :===\n", toppers)