from abc import ABC , abstractmethod
from datetime import datetime

class Person:

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

class Customer(Person):

    def __init__(self,name,age,address,customer_id):
        super().__init__(name,age,address)
        self.customer_id=customer_id

#       ABC



class Account(ABC):
    __total_account=0
    def __init__(self,account_number,account_holder,balance=0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.__balance=balance
        Account.__total_account+=1
        self.Transaction = []

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
        self.__balance = amount


    def deposite(self,amount):
        if amount > 0:
            self.balance+=amount
            self.Transaction.append(F"{datetime.now()} | Deposite | {amount}")
        else: 
            print("Invalid Amount !")

    @abstractmethod
    def withdraw(self,amount):
        pass

    @staticmethod
    def get_no_account():
        return Account.__total_account


class SavingAccount(Account):

    def __init__(self,account_number,account_holder,interest_rate,balance=0):
        super().__init__(account_number,account_holder,balance)
        self.interest_rate=interest_rate

    def deposite(self, amount):
        if amount <= 0:
            print("Invalid deposit amount!")
            return
        self.balance += amount
        self.Transaction.append(F"{datetime.now()} | Deposit | {amount}")

    def add_interest(self):
        interestamount = (self.balance * self.interest_rate) /100
        self.balance += interestamount
        self.Transaction.append(F"{datetime.now()} | Interest | {interestamount}")

#               withdraw

    def withdraw(self,amount):
        if self.balance < amount:
            print("Invalid amount for withdraw ! ")
        else:
            self.balance -= amount
            self.Transaction.append(F"{datetime.now()} | Withdraw | {amount}")

    def account_type(self):
        return "Saving"



class CurrentAccount(Account):

    def __init__(self, account_number, account_holder,overdraft_limit ,balance=0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.Transaction.append(F"{datetime.now()} | Withdraw | {amount}")
        else:
            if self.balance + self.overdraft_limit > amount:
                self.balance -= amount
                self.overdraft_limit = self.overdraft_limit + self.balance
                self.Transaction.append(F"{datetime.now()} | Withdraw | {amount}")
            else:
                print("Invalid amount for withdraw !")
        

    def account_type(self):
        return "Current"




class Bank:

    def __init__(self):
        self.customer = []
        self.accounts = []

    def add_customer(self,customer):
        self.customer.append(customer)

    def add_account(self,account):
        self.accounts.append(account)

    def count_no_account(self):
        print(Account.get_no_account())

    def __len__(self):
        return len(self.customer)

    def transfar(self,acc_self,acc_no,amount):

        for i in self.accounts:
            if acc_self == i.account_number:
                if i.balance >= amount:
                    for j in self.accounts:
                        if acc_no == j.account_number:
                            i.Transaction.append(F"{datetime.now()} | Transfar Recive | {amount}")
                            j.balance += amount
                            break
                    i.balance -= amount
                    i.Transaction.append(F"{datetime.now()} | Transfar Sent | {amount}")
                    break
                else:
                    print("Invalid !")



my_bank1 = Bank()

a1 = SavingAccount(12321116,"alay",5,10000)
a2 = CurrentAccount(4946464,"avinash",5000,20000)
a3 = SavingAccount(4846464,"krish",5,15000)

my_bank1.add_account(a1)
my_bank1.add_account(a2)
my_bank1.add_account(a3)




while True:

    print("""====== Bank Management System ======
1. Create New Account
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Check Balance
6. Print Statement
7. View Total Accounts (classmethod)
8. Exit""")

    choice = int(input("\nEnter the choice : "))

    if choice == 1:
        print("\n====Enter Your Details====\n")
        cus_name=str(input("Enter your Name :> "))
        cus_age = int(input("Enter the your Age :> "))
        cus_addre = str(input("Enter your Address :>"))
        cus_ID = int(input("Enter your Customer ID :> "))

        cus_obj = Customer(cus_name,cus_age,cus_addre,cus_ID)
        my_bank1.add_customer(cus_obj)

        # Acc

        print("\n1 > Saving Account \n2 > Current Account")

        sub_choi = int(input("Enter your choice for Account Type :> "))


        if sub_choi ==1:

            interest = int(input("\nEnter your interest Rate :> "))
            balance = int(input("Enter your Balance :> "))
            sav_acc = int(input("Enter your Account Number :> "))

            acc_obj = SavingAccount(sav_acc,cus_name,interest,balance)
            my_bank1.add_account(acc_obj)

            print("\nYour Account is successfully Created !")

        elif sub_choi == 2:

            overd = int(input("\nEnter The limit of Overdraft :> "))
            balance = int(input("Enter your Balance :> "))
            cur_acc = int(input("Enter your Account Number :> "))

            acc_obj1 = CurrentAccount(cur_acc,cus_name,overd,balance)
            my_bank1.add_account(acc_obj1)

            print("Your Account is successfully Created !")


            
    elif choice == 2:
        acc_no =int(input("\nEnter your Account Number :> "))
        amount = int(input("Enter the amount for Deposite :> "))
        account_found = False

        for i in my_bank1.accounts:
            if i.account_number == acc_no:
                account_found = True
                i.deposite(amount)
                print("Amount successfully Deposite")
                break 
        if account_found == False:
            print("Account Not found !")

    elif choice == 3:
        acc_no =int(input("\nEnter your Account Number :> "))
        amount = int(input("Enter the amount for Withdraw :> "))
        account_found= False

        for i in my_bank1.accounts:
            if i.account_number == acc_no:
                account_found = True
                i.withdraw(amount)
                print("Amount successfully Withdraw") 
                break

        if account_found==False:
            print("Account Not found !")
        
    elif choice == 4:
        acc_self =int(input("\nEnter your Account Number :> "))
        acc_no = int(input("Enter the Other Account Number :> "))
        amount = int(input("Enter the amount for Transfar :> "))

        my_bank1.transfar(acc_self,acc_no,amount)
        print("Money Transfar is Completed !")

    elif choice == 5:
        acc_no =int(input("\nEnter your Account Number :> "))
        account_found = False
        
        for i in my_bank1.accounts:
            if i.account_number == acc_no:
                account_found = True
                print(f"{i.account_holder} your balance is {i.balance}")
                break

        if account_found == False:
            print("Account is not found !")
        
    elif choice == 6:
        acc_no =int(input("\nEnter Account Number :> "))
        account_found = False
        for i in my_bank1.accounts:
            if i.account_number == acc_no:
                account_found = True 

                print(f"""==== Print Statement ====
                Account Number : {i.account_number} || Account Type : {i.acoount_type} || Account Balance : {i.balance}""")
                if len(i.Transaction) > 0:
                    for j in i.Transaction:
                        print(j)
                break

        if account_found == False:
            print("Account is not Found !")


                    
    elif choice == 7:
        print(f"\nThe total Bank Accounts are {my_bank1.count_no_account()}")
    elif choice == 8:
        print("\nYou exited successfully !")
        break
    else:
        print("\nInvalid Choice !")
        break