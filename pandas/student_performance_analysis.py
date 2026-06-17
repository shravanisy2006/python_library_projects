import numpy as np
import pandas as pd

d = {
    "Student_id" : [101 , 102 , 103 , 104 , 105 , 106 , 107 , 108 , 109 , 110],
    "Name" : ['Shreya' , 'Rahil' , 'Sparsh' , 'Aaradhya' , 'Aditi' , 'Medini' , 'Avnish' , 'Arnav' , 'Shivam' , 'Soham'],
    "Department" : ['CSE' , 'Mech' , 'CSE' , 'AI' , 'ENTC' , 'AI' , 'CSE' , 'Mech' , 'ENTC' , 'CSE'],
    "Marks" : [83 , 79 , 86 , 56 , 98 , 69 , 70 , 79 , 78 , 80],
    "Attendance": [53.9 , 78 , 97 , 91 , 66.6 , 89 , 88 , 88.2 , 95 , 83]
}

index = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
df = pd.DataFrame(d , index)
print(df)

print("\n")

print("=== Top 3 students ===\n")
top_students = df.nlargest(3 , "Marks")
print(top_students)

print("\n")

print("=== Bottom 3 students ===\n")
bottom_students = df.nsmallest(3 , "Marks")
print(bottom_students)

print("\n")

avg = df["Marks"].mean()
above_average = df[df["Marks"] > avg]
print("=== Students marks above average===\n")
print(above_average)

print("\n")

dept_avg = df.groupby("Department")["Marks"].mean()
print("=== Department wise average marks===\n")
print(dept_avg)

print("\n")

attendance_comp = df[df["Attendance"] > 85]
print("=== Students above 85 percent attendance ===\n")
print(attendance_comp)

print("\n")

dept_topper = df.loc[df.groupby("Department")["Marks"].idxmax()]
print("=== Department toppers ===\n")
print(dept_topper)

print("\n")

best_dept = dept_avg.idxmax()
print("=== Best Department ===\n")
print(best_dept)