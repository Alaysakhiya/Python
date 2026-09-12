import random

print("""
Random Data Generation :
1. Generate Random Number
2. Generate Random List 
3. Create Random Password
4. Generate Random OTP
5. Back Main Manu

""")

while True:

    choice = int(input("Enter your Choice :> "))
    
    if choice == 1:
        
            print(random.randint(100,1000))

    elif choice == 2:
            
            num =int(input("Enter the num:> "))
            li = random.choices(range(100),k=num)
            print(f"Your List {li}")

    elif choice == 3:
                
            charactar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#&"
            num =int(input("Enter the Password Length (8=>) :> "))

            li = random.choices(range(100),k=num)
            print(f"Your Password is {li}")


    elif choice == 4:
            print(f"Your OTP is {random.randint(1001,9999)}")

    elif choice == 5:
            print("Return Back to Main Manu ")
            break
            
    else:
            print("Invalid !")