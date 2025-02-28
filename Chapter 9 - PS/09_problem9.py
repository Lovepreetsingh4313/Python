# Write a program to find out whether a file is identical & matches the content of another file.

with open("this.txt") as f:
    content = f.read()

with open("this.copy.txt") as f:
    contentNew = f.read()

if(content == contentNew):
    print("Identical")

else:
    print("not Identical")            