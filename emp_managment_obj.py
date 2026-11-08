employees = [
    {"id":1,"emp_name":"dhruv","department":"developer","skills":["python","ruby"]},
    {"id":2,"emp_name":"joel","department":"admin","skills":["devops","jenkins"]}
    ]

class Employee:
    def __init__(self,emp_id,emp_name,dept,skills):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.dept = dept
        self.skills = skills
   

    def add_employee(self):
        if self.emp_id not in set(emp["id"] for emp in employees):
            employees.append({"id":self.emp_id,"emp_name":self.emp_name,"department":self.dept,"skills":[self.skills]})
            print("employee added")
        else:
            print("employee already existed")

    def viewEmployees():
        print("The Employees list")
        for emp in employees:
            print("id:",emp["id"],"Emp_name:",emp["emp_name"],"department:",emp["department"],"skills:",
        emp["skills"])

    def searchEmp(emp_id):
        for emp in employees:
            if emp["id"] == emp_id:
                print("Employee found")
                print("id:", emp["id"], "Emp_name:", emp["emp_name"], "department:", emp["department"], "skills:", emp["skills"])
                return
        print("Employee not found")


    def removeEmp(emp_id):
        for emp in employees:
            if emp["id"] == emp_id:
                employees.remove(emp)
                print("The employee id",emp_id,"is removed")
            return
        print("The employee not found")


    def dept_skills():
        print("Departments:")
        for emp in employees:
            print(emp["department"])
    
        print("skills:")
        for emp in employees:
            print(emp["skills"])

while True:
    print("Menu")
    print("1.add_employee ")
    print("2.View employees ")
    print("3. Search employee ")
    print("4. remove employee ")
    print("5. dept skills ")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter employee ID: "))
        emp_name = input("Enter Name: ")
        dept = input("Enter department: ")
        skills = list(input("Enter skills: ").split(','))
        emp1 = Employee(emp_id,emp_name,dept,skills)
        emp1.add_employee()
    elif choice == 2:
        Employee.viewEmployees()
    elif choice == 3:
        emp_id = int(input("Enter Employee ID to Search: "))
        Employee.searchEmp(emp_id)
    elif choice == 4:
        emp_id = int(input("Enter Employee ID to Remove: "))
        Employee.removeEmp(emp_id)
    elif choice == 5:
        Employee.dept_skills()
    elif choice == 6:
        print("Thank you")
        break







