class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

e = Employee()
e.a = 100
e.show()        