# Write a program to make a copy of a text file “this. txt”

with open("this.txt") as f:
    content = f.read()

with open("this.copy.txt", "w") as f:
    contentNew = f.write(content)    