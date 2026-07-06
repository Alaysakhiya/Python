
print("----Python Oop Project: Employee Management System---- ")


class Employee():

    def __init__(self,name,age,salary,emId):
        self.__name=name
        self.__age=age
        self.__salary=salary
        self.__emId=emId

    def showInfo(self):

        print(F"Employee ID is {self.__emId} || Employee name is {self.__name} || Age of Employee is {self.__age} || Salary of Employee is {self.__salary}")

    def __del__(self):
        pass


class Manager(Employee):

    def __init__(self, name, age, salary, emId ,department):
        super().__init__(name, age, salary, emId)

        self.__department=department

    def showInfo(self):
        super().showInfo()
        print(F"Manager Department is {self.__department}")

    def __del__(self):
        pass
    
class Developer(Employee):

    def __init__(self, name, age, salary, emId ,programming):
        super().__init__(name, age, salary, emId)

        self.__programming=programming

    def showInfo(self):
        super().showInfo()
        print(F"Developer is in {self.__programming} language")

    def __del__(self):
        pass


em=[]
man=[]
dev=[]


while True:

    print('''
    ---Select the operation---
          
1. Creata an Employee
2. Create a Manager
3. Create a Developer
4. To View
0. To Exit
          ''')
    
    choice=int(input("Enter the choice => "))


    if choice==1:
        name=input("Enter the Emoloyee Name :> ")
        age=int(input("Enter the Emoloyee Age:> "))
        salary=int(input("Enter the Emoloyee Salary :> "))
        emId=int(input("Enter the Employee Id :> "))

        emobj=Employee(name,age,salary,emId)

        em.append(emobj)

        print("\nEmployee is Created !")

    elif choice==2:

        name=input("Enter the Manager Name => " )
        age=int(input("Enter the Manager Age => " ))
        salary=int(input("Enter the Manager Salary => " ))
        emId=int(input("Enter the Manager ID => " ))
        department=input("Enter the Manager Department => ")

        manobj=Manager(name,age,salary,emId,department)

        man.append(manobj)
        
        print("\nManager is Created ! ")


    elif choice==3:

        name=input("Enter the Developer Name => " )
        age=int(input("Enter the Developer Age => " ))
        salary=int(input("Enter the Developer Salary => " ))
        emId=int(input("Enter the Developer ID => " ))
        programming=input("Enter the Developer Programming Language => ")

        devobj=Developer(name,age,salary,emId,programming)

        dev.append(devobj)

        print("\nDeveloper is Created ! ")


    elif choice==4:
        
        subChoice=int(input("Enter 1/2/3 to view Emp/Man/Dev :> "))

        if subChoice==1:
            for i in em:
                i.showInfo()

        elif subChoice==2:

            for i in man:
                i.showInfo()
        elif subChoice==3:

            for i in dev:
                i.showInfo()

        else:
            print("\nInvalid choice !")


 

    elif choice==0:

        print("\nYou suucessfully Exited the Programme")
        break

    else:
        print("\nInvalid choice !")
        break


