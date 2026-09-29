
# import random

# amount = int(input("Enter The Base Amount :> "))
# interest_rate = int(input("Enter The  Rate of Interest in (%) :> "))
# year = int(input("Enter the Duration (in Year) :> "))

# base_amount = amount

# for i in range(year):
#     interest = (amount * interest_rate)/100
#     amount+=interest

# print(f"Compound Interest :> {amount - base_amount}")
# print(f"Final Amount :> {amount}")

# angel = int(input("Enter the Degree to Calculate Trigonometric :>  "))

# data = math.radians(angel)

# print(f"Sin{angel}° Value is {math.sin(data)}")
# print(f"Cos{angel}° Value is {math.cos(data)}")
# print(f"Tan{angel}° Value is {math.tan(data)}")

# print(random.randint(1000,10000))
# num =int(input("Enter the num:> "))
# li = random.choices(range(100),k=num)

# print(li)

# print(f"Your OTP is {random.randint(1001,9999)}")

# import uuid
# import math

# print(uuid.uuid4())
# name = input("Enter File Name (.txt) :> ")
# path = f"D:\\Python\\Project\\Module_packeg_Project\\{name}"


# data = input("Enter the Data to Write :> ")
# with open(f"{path}","a") as file:
#     file.write(data)
    
import numpy as np

print("Select the type of Array to create :>")
print("1. 1D Array") 
print("2. 2D Array") 
print("3. 3D Array")

sub_choice = int(input("\nEnter the Choice :> "))

if sub_choice == 1:
    ele1 = input("Enter the Element of the array separated by space :> ")
    a1 = np.array(list(map(int,ele1.split())))
    print("Array Created Successfully :")
    print(a1)

elif sub_choice == 2:
    row1 = int(input("Enter the number of Row :> "))
    col1 =int(input("Enter the number of Columns :> "))

    ele2 = input(f"Enter {row1 * col1} elements for the array separated bt space :> ")
    a1 = np.array(list(map(int,ele2.split()))).reshape(row1,col1)
    print("Array Created Successfully :")
    print(a1)

