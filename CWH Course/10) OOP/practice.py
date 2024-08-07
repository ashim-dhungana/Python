class Programmer:
    company = "microsoft"
    department = "python"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

new = Programmer("Tony",100000)
new2 = Programmer("Steve",20000)


print(new.company, new.department, new.salary, new.name)