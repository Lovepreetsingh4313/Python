def goodday(name, ending):
    print("Good Day, " + name)
    print(ending)

goodday("Lovepreet", "Thank You")    
goodday("Manna", "Satshriakal")    
goodday("Dilpreet", "Namaste")    

########################################################

# Return function

def goodday(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "Done"

a = goodday("Lovepreet", "Thank You")    
print(a)