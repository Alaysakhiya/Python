from abc import ABC , abstractmethod
from datetime import datetime

class Person:

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

class Customer(Person):

    def __init__(self,name,age,address,customer_id):
        super.__init__(self,name,age,address)
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
        if amount < 0:
            print("Invalid Deposite amount !")
        else:
            self.balance+=amount
            self.Transaction.append(F"{datetime} | Deposite | {amount}")


    @abstractmethod
    def withdraw(self,amount):
        pass


class SavingAccount(Account):

    def __init__(self,account_number,account_holder,balance,interest_rate):
        super().__init__(account_number,account_holder,balance)
        self.interest_rate=interest_rate

    def add_interest(self):
        interestamount = (self.balance * self.interest_rate) /100
        self.balance += interestamount
        self.Transaction.append(F"{datetime} | Interest | {interestamount}")

#               deposite

    def deposite(self, amount):
        super().deposite(amount)
        
        
#               withdraw

    def withdraw(self,amount):
        if self.balance < amount:
            print("Invalid amount for withdraw ! ")
        else:
            self.balance -= amount
            self.Transaction.append(F"{datetime} | Withdraw | {amount}")



class CurrentAccount(Account):

    def __init__(self, account_number, account_holder, balance,overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit


    def deposite(self, amount):
        super().deposite(amount)
        print(self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.Transaction.append(F"{datetime} | Withdraw | {amount}")
        else:
            if amount > self.balance + self.overdraft_limit:
                
                self.Transaction.append(F"{datetime} | Withdraw | {amount}")
            else:
                print("Invalid amount for withdraw !")
        print(self.balance)


# p1 = SavingAccount(5464,"bdfb",10000,5)
# p1.deposite(2000)
p1 = CurrentAccount(6564646,"dgfd",10000,2000)
p1.balance
p1.deposite(2000)
p1.withdraw(12000)
print(p1.overdraft_limit)
print(p1.Transaction)






# while True:

#     print("""====== Bank Management System ======
# 1. Create New Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. Transfer Money
# 5. Check Balance
# 6. Print Statement
# 7. View Total Accounts (classmethod)
# 8. Exit""")

#     choice = int(input("Enter the choice : "))

#     if choice == 1:
#         pass
#     elif choice == 2:
#         pass
#     elif choice == 3:
#         pass
#     elif choice == 4:
#          pass
#     elif choice == 5:
#          pass
#     elif choice == 6:
#          pass
#     elif choice == 7:
#          pass
#     elif choice == 8:
#          pass""""
