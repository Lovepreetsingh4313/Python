# Write a program to find out the line number where python is present from ques 6.

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
found = False

for line in lines:
    if("python" in line):
        print(f"Python is present. Line no: {lineno}")
        found = True           # we can use break here 
    lineno += 1
         
if not found:
    print("Python is not present")
# else:
#     print("Python is not present")  # This is used with break statement       
