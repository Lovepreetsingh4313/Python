# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘Twinkle’

f = open("poems.txt")
content = f.read()
if("Twinkle" in content):
    print("The word Twinkle is present in the content")

else:
    print("The word Twinkle is not present in the content")
     
f.close()     
       