# Write a program to accept marks of 6 students and display them in a sorted manner

Marks = []

S1 = int(input("Enter Student Marks: "))
Marks.append(S1)
S2 = int(input("Enter Student Marks: "))
Marks.append(S2)
S3 = int(input("Enter Student Marks: "))
Marks.append(S3)
S4 = int(input("Enter Student Marks: "))
Marks.append(S4)
S5 = int(input("Enter Student Marks: "))
Marks.append(S5)
S6 = int(input("Enter Student Marks: "))
Marks.append(S6)

Marks.sort()

print(Marks)