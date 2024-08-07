class Employee:
    name = "Ashim"  #class attribute
    language = "Everything"
    salary = 100000

    def __init__(self):     #always runs automatically
        print("This is a constructor")

    def getInfo(self):
        print(f"The language is {self.language} & the salary is {self.salary}")

new = Employee()
print(new.name, new.salary)

new.name = "King"   #instance attribute
print(new.name, new.salary)

new.getInfo()