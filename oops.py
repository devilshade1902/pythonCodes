# class Person:
#     def display(self):
#         name = "dhruv"
#         print("name: ", name)



# person1 = Person()
# person1.display()

# person2 = Person()
# person2.display()

class Person:
    def __init__(self,p_name,p_age,p_email):
        self.p_name = p_name
        self.p_age = p_age
        self.p_email = p_email


p1 = Person("dhruv",19,"dhruv@gmail.com")
print(p1.p_name)

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


