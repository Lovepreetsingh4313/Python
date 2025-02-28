class Employee:
    language = "Py" # This is a class attribute
    salary = "100000"

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
     
    @staticmethod 
    def greet():
        print("Good Morning")    

lovi = Employee()
# lovi.language = "Java" # This is an instance(object) attribute
print(lovi.language, lovi.salary)   
lovi.getInfo()
lovi.greet()