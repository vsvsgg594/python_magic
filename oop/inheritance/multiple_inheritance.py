class Job:
    def __init__(self,salary):
        self.salary = salary
    def display_salary(self):
        print(f'for this role your salary is {self.salary}')  
class Employee:
    def __init__(self,name):
        self.name = name
    def display_emp_name(self):
        print(f'your name is {self.name}')
class EmployeeJob(Job,Employee):
    def __init__(self,salary,name):
        Job.__init__(self,salary)
        Employee.__init__(self,name)
emp=EmployeeJob(123,"software engineering")    
emp.display_salary()
emp.display_emp_name()  


# Hybrid Inheritance (Multiple + Multilevel)
