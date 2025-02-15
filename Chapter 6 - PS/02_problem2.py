# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

math = int(input("Enter math marks: "))
physcis = int(input("Enter physics marks: "))
chemistry = int(input("Enter chemistry marks: "))

# Check for  total percentage
total_percentage = (100)*(math+physcis+chemistry)/300


if(total_percentage >= 40 and math>=33 and physcis>=33 and chemistry>=33):
    print("Student has passed: ", total_percentage)

else:
    print("Student has failed: ", total_percentage)