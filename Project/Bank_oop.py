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
            self.Transaction.append(F"{datetime.now()} | Deposite | {amount}")


    @abstractmethod
    def withdraw(self,amount):
        pass

    @staticmethod
    def get_no_account():
        return Account.__total_account


class SavingAccount(Account):

    def __init__(self,account_number,account_holder,balance,interest_rate):
        super().__init__(account_number,account_holder,balance)
        self.interest_rate=interest_rate

    def add_interest(self):
        interestamount = (self.balance * self.interest_rate) /100
        self.balance += interestamount
        self.Transaction.append(F"{datetime} | Interest | {interestamount}")

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

    def __init__(self, account_number, account_holder, balance,overdraft_limit):
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

    customer = []
    accounts = []

    def add_customer(self,customer):
        self.customer.append(customer)

    def add_account(self,account):
        self.accounts.append(account)

    def count_no_account(self):
        print(Account.get_no_account)

    def __len__(self):
        return len(self.customer)

    def transfar(self,acc_self,acc_no,amount):

        for i in self.accounts:
            if acc_self == i.account_number:
                if i.balance >= amount:
                    for j in self.accounts:
                        if acc_no == j.account_number:
                            self.Transaction.append(F"{datetime.now()} | Get transfar Money | {amount}")
                            j.balance += amount
                            break
                    i.balance -= amount
                    self.Transaction.append(F"{datetime.now()} | Transfar Money | {amount}")
                    break
                else:
                    print("Invalid !")



my_bank1 = Bank()

a1 = SavingAccount(12321116,"alay",10000,5)
a2 = CurrentAccount(4946464,"avinash",20000,5000)
a3 = SavingAccount(4846464,"krish",15000,5)

my_bank1.add_account(a1)
my_bank1.add_account(a2)
my_bank1.add_account(a3)
my_bank1.transfar(4946464,4846464,5000)
print(a1.balance)
print(a2.balance)
print(a3.balance)




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

    choice = int(input("Enter the choice : "))

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        pass
