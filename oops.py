# class Person:
#     def display(self):
#         name = "dhruv"
#         print("name: ", name)



# person1 = Person()
# person1.display()

# person2 = Person()
# person2.display()

# class Person:
#     def __init__(self,p_name,p_age,p_email):
#         self.p_name = p_name
#         self.p_age = p_age
#         self.p_email = p_email


# p1 = Person("dhruv",19,"dhruv@gmail.com")
# print(p1.p_name)

# p2 = Person()
# p2.p_name = 'deepika'
# p2.p_age = 27
# p2.p_email = 'deepika@gmail.com'
# print(p2.p_email)                  
# p2 = Person()
# TypeError: Person.__init__() missing 3 required positional arguments: 'p_name', 'p_age', and 'p_email'

# class Employee():
#     def __init__(self,empno,ename,esal):
#         # self.empno = 1
#         # self.ename = "abc"
#         # self.esal = 0.0
#         self.empno = empno
#         self.ename = ename
#         self.esal = esal

#     def display(self):
#         print(self.empno, " : ",self.ename," : ", self.esal)
    
#     def acceptEmployeeInfo(self):
#         self.ename = input("Enter a value for name: ")
#         self.empno = int(input("Enter a value for empno: "))
#         self.esal = input("Enter a value for esal: ")


# emp1 = Employee(12,"deepikar",3456)
# emp1.display()

# emp1.acceptEmployeeInfo()
# emp1.display()



# class Product:
#     def __init__(self,p_id,p_name,p_price,p_quantity):
#         self.p_id = p_id
#         self.p_name = 'brush'
#         self.p_price = 200
#         self.p_quantity = 100

    
#     def acceptProductInfo(self):
#         self.p_id = int(input("Enter product id: "))
#         self.p_name = input("Enter product name: ")
#         self.p_price = input("Enter product price: ")
#         self.p_quantity = input("Enter product quantity: ")

#     def display(self):
#         print(self.p_name, " : " , self.p_price, "quantity: ",self.p_quantity)


# product1 = Product(1,"toothpast",2000,1000)


# product1.acceptProductInfo()
# product1.display()


# class Person:
#     def __init__(self,p_name,p_age,p_marks1,p_marks2,p_marks3):
#         self.p_name = p_name
#         self.p_age = p_age
#         self.p_marks1 = 0
#         self.p_marks2 = 0
#         self.p_marks3 = 0

#     def acceptStudentInfo(self):
#         self.p_name = input("Enter Your name : ")
#         self.p_age = int(input("Enter your age: "))
#         self.p_marks1 = int(input("Enter your marks for 1: "))
#         self.p_marks2 = int(input("Enter your marks for 2: "))
#         self.p_marks3 = int(input("Enter your marks for 3: "))


#     def displayStudentInfo(self):
#         print("Student name : ",self.p_name, "age is",self.p_age, "and the marks for 1 2 3 are ",self.p_marks1,self.p_marks2,self.p_marks3)
    
#     def totalmarks(self):
#         self.total = self.p_marks1+self.p_marks2+self.p_marks3
#         return self.total

#     def calculateAvg(self,total):
#         avg = total/3
#         print("The avg marks are: ",avg)



# student1 = Person("dhruv",19,12,34,50)
# # student1.displayStudentInfo()

# student1.acceptStudentInfo()
# total = student1.totalmarks()
# student1.displayStudentInfo()
# student1.calculateAvg(total)


# class Employee:
#     def __init__(self,empno,ename,esal,ecomm,hra,da,deptno):
#         self.empno = empno
#         self.ename = ename
#         self.esal = 0
#         self.ecomm = 0
#         self.hra = 0
#         self.da = 0
#         self.deptno = 0

#     def acceptEmployeeInfo(self):
#         self.empno = int(input("Enter your empno: "))
#         self.ename = input("Enter your name: ")
#         self.esal = int(input("Enter your salary: "))
#         self.ecomm = int(input("Enter your ecomm: "))
#         self.hra = int(input("Enter your hra: "))
#         self.da = int(input("Enter your da: "))
#         self.deptno = int(input("Enter your deptno: "))
    
#     def displayEmployeeInfo(self):
#         print("empno: ",self.empno)
#         print("ename: ",self.ename)
#         print("esal: ",self.esal)
#         print("ecomm: ",self.ecomm)
#         print("hra: ",self.hra)
#         print("da: ",self.da)
#         print("deptno: ",self.deptno)
    
#     def calculateBasicSalary(self):
#         self.basicSalary = self.esal+self.ecomm+self.hra+self.da
#         return int(self.basicSalary)
    
#     def calculateGrossSalary(self,basicSalary):
#         self.grosssalary = basicSalary * 12
#         print(self.grosssalary)



# emp1 = Employee(1,"dhruv",2000,200,30,10,100)
# emp1.acceptEmployeeInfo()
# emp1.displayEmployeeInfo()
# basicSalary=emp1.calculateBasicSalary()
# emp1.calculateGrossSalary(basicSalary)



# class Testmaths:
#     def __init__(self,num1,num2):
#         self.n1 = num1
#         self.n2 = num2
    
#     def addition(self,n1,n2):
#         self.result = n1+n2
#         print("addition : ",self.result)
    
#     def __del__(self):
#         print("object in destruction mode")
    
# tm = Testmaths(0,0)
# tm.addition(12,12)


# class Person:
#     def __init__(self,name,age,email):
#         self.name = name
#         self.age = age
#         self.email = email

#     def display_info(self):
#         print("person name: ",self.name,"age: ",self.age,"email: ",self.email)
    

# class Employee(Person):
#     def acceptEmployeeInfo(self):
#         self.emp_id = int(input("Enter your Emp_id: "))
#         self.job = input("enter your job: ")
#         self.sal = int(input("Enter your basic salary: "))

#     def calculateGrossSalary(self):
#         self.grossSal = self.sal *12
#         print("Total salary of employee : ",self.grossSal)
    
#     def displayEmployee(self):
#         print("Employee id : ",self.emp_id, "job : ",self.job,"basic salary : ",self.sal)



# emp1 = Employee("dhruv",30,"dhruv@gmail.com")
# emp1.display_info()
# emp1.acceptEmployeeInfo()
# emp1.display_info()
# emp1.calculateGrossSalary()

# class Person:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
    
#     def displayPersonInfo(self):
#         print("Person name :", self.name, "and email :", self.email)


# class Student(Person):
#     def __init__(self, name, email,m1,m2,m3):
#         super().__init__(name, email)
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def calculateTotal(self):
#         self.total = self.m1 + self.m2 + self.m3
#         print("Total of marks: ",self.total)


# stud1  = Student("dhruv","dhruv@gmail.com",20,30,40)
# stud1.displayPersonInfo()
# stud1.calculateTotal()

# class Teacher:
#     def __init__(self,name,subject):
#         self.name = name
#         self.subject = subject
    
#     def displayTeacherDetails(self):
#         print("Teacher name : ",self.name,"subject : ",self.subject)
    

# class Dancer:
#     def __init__(self,name,academy):
#         self.name = name
#         self.academy = academy

#     def displayDanceDetails(self):
#         print("Dancer name :",self.name,"academy: ",self.academy)
    

# class DanceTeacher(Teacher,Dancer):
#     def __init__(self, name, subject,academy):
#         Teacher.__init__(self,name, subject)
#         Dancer.__init__(self,name, academy)


# danceteacher1 = DanceTeacher("dhruv","hiphop","ABCD")
# danceteacher1.displayTeacherDetails()
# danceteacher1.displayDanceDetails()

# multilevel
# class Person:
#     def __init__(self,name):
#         self.name = name
    
#     def displayname(self):
#         print("Name of the person is : ", self.name)
    

# class Employee(Person):
#     def __init__(self, name,company):
#         super().__init__(name)
#         self.company = company
    
#     def displayEmp(self):
#         print("the name of the employee is ",self.name,"and the company is ",self.company)

# class Freelancer(Employee):
#     def __init__(self, name, company,sal):
#         super().__init__(name, company)
#         self.sal = sal
    
#     def displayFreelance(self):
#         print("the employee name is ",self.name,"and the company is ",
#               self.company,"and the salary is ",self.sal)



# free1 = Freelancer("dhruv","tata",30000)
# free1.displayEmp()
# free1.displayFreelance()
# free1.displayname()
# emp1 = Employee("dhruv","google")
# emp1.displayname()
# emp1.displayEmp()
# hierarachal

# class Person:
#     def __init__(self,name):
#         self.name = name
    
#     def displayname(self):
#         print("Name of the person is : ", self.name)
    
# class Student(Person):
#     def __init__(self, name,rollno,subject):
#         super().__init__(name)
#         self.rollno = rollno
#         self.subject = subject
    
#     def displayStudentsInfo(self):
#         print("the name of the student is ",self.name,"and the roll no: ",
#               self.rollno,"and the subject is ",self.subject)

# class Employee(Person):
#     def __init__(self, name,dept):
#         super().__init__(name)
#         self.dept = dept

#     def displayEmployee(self):
#         print("the name of the employee is ",self.name,"and the dept is ",self.dept)


# stud1 = Student("dhruv",20,"maths")
# stud1.displayname()
# stud1.displayStudentsInfo()
# emp1 = Employee("dhruv","developer")
# emp1.displayname()
# emp1.displayEmployee()

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start():
        pass
    
    def stop():
        pass

class Car(Vehicle):
    def start(self):
        print("car engine started")
    
    def stop(self):
        print("car engine stopped")


class Bike(Vehicle):
    pass


car1 = Car()
car1.start()
car1.stop()

bike1 = Bike()
bike1.start()
bike1.stop()