class Employee():

    id=100
    def __init__(self,employee_name,employee_age,employee_salary):
        self.employee_name=employee_name
        self.employee_age=employee_age
        self.__employee_salary=employee_salary  
        self.__employee_id=Employee.id

        Employee.id+=1


    def get_employee(self):
        return self.__employee_id
    
    def display_(self):

        if type(self).__name__ =="Employee":
            print(F"Employee ID : {self.__employee_id} || Employee Name : {self.employee_name} || Employee Age : {self.employee_age} || Employee salary : {self.__employee_salary}  ")

        elif type(self).__name__=="Manager": 
            print(F"Manager ID : {self.__employee_id} || Manager Name : {self.employee_name} || Manager Age : {self.employee_age} || Manager salary : {self.__employee_salary}  ")

        else:
            print(F"Developer ID : {self.__employee_id} || Developer Name : {self.employee_name} || Developer Age : {self.employee_age} || Developer salary : {self.__employee_salary}  ")

    def __del__(self):
        pass

class Manager(Employee):

    def __init__(self, employee_name, employee_age, employee_salary, Department):
        super().__init__(employee_name, employee_age, employee_salary)
        self.__department=Department


    def display_(self):
        super().display_()
        print(f"Manager Department : {self.__department}")

    def __del__(self):
        pass

class Developer(Employee):

    def __init__(self, employee_name, employee_age, employee_salary, Pro_language):
        super().__init__(employee_name, employee_age, employee_salary)
        self.__Programming_language=Pro_language


    def display_(self):
        super().display_()
        print(f"Developer Programming Language : {self.__Programming_language}")

    def __del__(self):
        pass


emp=[]
man=[]
dev=[]

print("----Python OOP Project: Employee Management System----")
    
while True:
    
    print("""
          ---Select an operation---
1. To Create Employee
2. To Create Manager
3. To Create Developer
4. To View
0. To Exit
          """)
    
    choice=int(input("Enter the Operation :> "))

    if choice==1:

        employee_name=input("Enter the Employee Name : ")
        employee_age=int(input("Enter the Age of the Employee : "))
        employee_salary=int(input("Enter the Salary of the Employee : "))


        empobj=Employee(employee_name,employee_age,employee_salary)

        emp.append(empobj)

        print("\nEmployee is Created !")


    elif choice==2:

        manager_name=input("Enter the Manager Name : ")
        manager_age=int(input("Enter the Age of the Manager : "))
        manager_salary=int(input("Enter the Salary of the Manager : "))
        manager_department=input("Enter the Department of Manager : ")


        manobj=Manager(manager_name,manager_age,manager_salary,manager_department)

        man.append(manobj)

        print("\nManager is Created !")

    elif choice==3:

        developer_name=input("Enter the Developer Name : ")
        developer_age=int(input("Enter the Age of the Developer : "))
        developer_salary=int(input("Enter the Salary of the Developer : "))
        developer_Language=input("Enter the Programming Language of Developer : ")


        devobj=Developer(developer_name,developer_age,developer_salary,developer_Language)

        dev.append(devobj)

        print("\nDeveloper is Created !")

    elif choice==4:

        subchoice=int(input("Enter 1/2/3 to View EMP/MAN/DEV :> "))

        if subchoice==1:

            for i in emp:
                i.display_()

        elif subchoice==2:

            for i in man:
                i.display_()

        elif subchoice==3:

            for i in dev:
                i.display_()
        else:
            print("\nEnter Valid choice !")


    elif choice==0:
        print("\nProgram is Closed !")
        break

    else:
        print("\nInvalid Choice !")
        break