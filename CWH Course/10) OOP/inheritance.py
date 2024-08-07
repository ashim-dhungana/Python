class Employee:
    salary = 20000
    def show(self,name,lang,):
        self.name = name 
        self.language = lang
        print(f"The name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    language = "python"
    def showLanguage(self):
        print(f"The salary is {self.salary} for language {self.language}")

a = Employee()
b = Programmer()

a.show("Tony","Python")
b.show("Steve","Java")
b.showLanguage()