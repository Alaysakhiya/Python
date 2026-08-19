from abc import ABC , abstractmethod

class Person:

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

class Customer(Person):

    Bank = "SBI"

    def __init__(self,name,age,address,customer_id):
        super.__init__(self,name,age,address)
        self.customer_id=customer_id

#       ABC


class Account(ABC):
    total_account=0
    def __init__(self,account_number,account_holder,balance=0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.__balance=balance
        Account.total_account+=1
        Transaction = []

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
        self.__balance += amount


    def deposite(self,Damount):
        self.Damount = Damount
        self.__balance += Damount
        print(F"{self.balance}")


    def withdraw(self,Withamount):
        self.Wamount = Withamount
        self.__balance -= Withamount
        print(F"{self.balance}")


class SavingAccount(Account):

    def __init__(self,account_number,account_holder,interest_rate,balance=0):
        super().__init__(account_number,account_holder,balance)
        self.interest_rate=interest_rate

    def add_interest(self,balance):
        super().__init__(balance)
        interest = {(self.balance * self.interest_rate)/100} 
        print({interest})


class CurrentAccount(Account):
    pass



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
#          pass