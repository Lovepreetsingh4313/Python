# Create a class “Programmer” for storing information of few programmers working at Microsoft

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Lovi", 110000, "L6S4G3")
print(p.name, p.salary, p.pin, p.company)        

r = Programmer("Rohan", 100000, 140001)
print(r.name, r.salary, r.pin, r.company)