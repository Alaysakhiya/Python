#          1
class Person:


    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):

    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno

    def displayData(self):
        print(F"Name : {self.name} | Age : {self.age} | Roll No : {self.rollno}")


stu= Student("Alay",32,101)
stu.displayData()


#           2

class Vehicle:


    def __init__(self,Brand,Model):
        self.Brand=Brand
        self.Model=Model

class Car(Vehicle):

    def __init__(self,Brand,Model,Fuel_type):
        super().__init__(Brand,Model)
        self.Fuel_type=Fuel_type

    def displayData(self):
        print(F"Brand : {self.Brand} | Model : {self.Model} | Fuel Type : {self.Fuel_type}")


car1=Car("TATA","Punch","CNG")
car1.displayData()

#           3

class Employee:

    def __init__(self,Name,Salary):
        self.Name=Name
        self.Salary=Salary

class Manager(Employee):

    def __init__(self,Name,Salary,Department):
        super().__init__(Name,Salary)
        self.Department=Department

    def displayData(self):
        print(F"Name : {self.Name} | Salary : {self.Salary} | Department : {self.Department}")


em1=Manager("Avinash",30000,"HR")
em1.displayData()


#           4
class BankAccount:

    def __init__(self,Account_No,Holder_name,balance):
        self.Account_No=Account_No
        self.Holder_name=Holder_name
        self.balance=balance

class SavingAccount(BankAccount):

    def __init__(self,Account_No,Holder_name,balance,Interest_rate):
        super().__init__(Account_No,Holder_name,balance)
        self.balance=balance
        self.Interest_rate=Interest_rate

    def displayData(self):
        print(F"Account No. : {self.Account_No} | Holder Name : {self.Holder_name} | Balance : {self.balance}")
        print(F"Interest Rate : {self.Interest_rate}%  | Interest : {(self.balance*self.Interest_rate)/100} ")


Acc=SavingAccount(1001,"Alay",50000,5)
Acc.displayData()



#           5
class Product:

    def __init__(self,Product,Price):
        self.Product=Product
        self.Price=Price


class Electronics(Product):

    def __init__(self,Product,Price,Brand,Warranty):
        super().__init__(Product,Price)
        self.Brand=Brand
        self.Warranty=Warranty

    def displayData(self):
        print(F"Product : {self.Product} | Price : {self.Price} | Brand : {self.Brand} | Warranty : {self.Warranty} Years")


item=Electronics("Laptop",90000,"Lenovo",1)
item.displayData()
