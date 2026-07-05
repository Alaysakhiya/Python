class Employe():

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def showImfo(self):
        print(f"EMp name is {self.name} || EMp age is {self.age} || salary is {self.salary}")

    def __del__(self):
        pass

class Manager(Employe):

    def __init__(self,name,age,salary,department):
        super().__init__(name,age,salary)

        self.department=department


    def showInfo(self):
        super().showImfo()
        print(f"MAN department is {self.department}")


    def __del__(self):
        pass


class Developer(Employe):

    def __init__(self, name, age, salary,Programming):
        super().__init__(name, age, salary)
        self.programming=Programming


    def showImfo(self):
        super().showImfo()
        print(F"DEV language is {self.programming}")

    def __del__(self):
        pass



em=[]
man=[]
dev=[]


while True:


    Choice=int(input("enter the your choice => "))

    if Choice==1:

        name=input("Enter the name of employee => ")
        age=int(input("enter the Age of employee => "))
        salary=int(input("Enter the salary of employee =>"))


        emobj=Employe(name,age,salary)

        em.append(emobj)


        print("Employee is created !")


    elif Choice==2:

        name=input("Enter the name of MAnager => ")
        age=int(input("enter the Age of MAnager => "))
        salary=int(input("Enter the salary of managar => "))
        department=input("Enter the Department of MAnager => ")

        manobj=Manager(name,age,salary,department)

        man.append(manobj)


        print("MAnager  is created !")

    elif Choice==3:

        name=input("Enter the name of Developer => ")
        age=int(input("enter the Age of Developer => "))
        salary=int(input("Enter the salary of Developer => "))
        programming=input("Enter the programming language of Developer => ")

        devobj=Developer(name,age,salary,programming)

        dev.append(devobj)


        print("Developer is created !")


    elif Choice==4:
        subchoice=int(input("Enter 1/2/3 to view EMP/MAN/DEV => "))

        if subchoice==1:


            for i in em:
                i.showInfo()

        elif subchoice==2:

            for i in man:
                i.showInfo()


        elif subchoice==3:

            for i in dev:
                i.showInfo()


        else:
            print("Invalid !")




    elif Choice==5:
        delchoice=int(input("Enter 1/2/3 to delete EMP/MAN/DEV => "))

        if delchoice==1:
            emID=int(input("Enter the ID to Delete => "))

            for i in em:
                if i["emID"]==emID:
                    del i

        elif delchoice==2:
            emID=int(input("Enter the ID to Delete => "))

            for i in man:
                if i["emID"]==emID:
                    del i

        elif delchoice==3:
            emID=int(input("Enter the ID to Delete => "))

            for i in dev:
                if i["emID"]==emID:
                    del i
        else:
            print("INvalid !")




    elif Choice==6:

        print("Programme Exited !")
        break

    else:
        print("Invalid !")

        break





        

