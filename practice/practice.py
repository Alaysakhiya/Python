# age= int(input("Enter the age :"))

# if age>=18:
#     print("you can vote")
# else:
#     print("you cna not vote")

# print("programme is ended")

# num = int(input("Enter the number: "))

# if num>0 and num%2 ==0:
#     print(f"{num} is a even number")
    
# else:
#     print(f"{num} is odd number")

# text = input("enter some text:")

# if text:
#     print("you enter the :",text)
# else:
#     print("you enter empty string")

# mark=int(input("Enter the mark :"))

# if mark >=90:
#     print("Grade = A")
# elif mark >=75:
#     print("Grade = B")
# elif mark >=60:
#     print("Grade = C")
# elif mark >=45:
#     print("Grade = D")
# else:
#     print("Grade = F")

# Eng = 45

# maths = 5

# science =8




# if Eng>= 50:
#     if maths>=50:
#         if science>=50:
#             print("You passed all subjects")

       
#         else:
#             print("you failed in science")
#     else:
#         print("you  failed in maths")
# else:
#     print("you failed in english")        


# num =int(input("Enter the num :"))

# result = "Even"if num%2 ==0 else"odd"

# print(result)

# eng = 78
# math=78
# sci=78

# if eng>math:
#     if eng>sci:
#         print("eng")
#     else:
#         print("sci")
# else:
#     if math>sci:
#         print("math")
#     else:
#         print("sci")                


# print("enter 1 to tea")
# print("Enter 2 to samosa")
# print("Enter 3 to pizza")


# choice=int(input("\n\nEnter the number to choice : "))

# match choice:
#     case 1:
#         print("you order the tea")
#     case 2:
#         print("you order the samosa")
#     case 3:
#         print("You order the pizza")
#     case _:
#         print("Invalid")    


# a =int(input("enter the 1 num :"))
# b =int(input("enter the 2 num :"))
# c =int(input("enter the 3 num :"))
# d = int(input("eenter the 4 num :"))


# if a>b:
#     if a>c:
#         if a>d:
#             print("A is largesst")
#         else:
#             print("D is largest")
#     else:
#         if c>b:
#             if c>d:
#                 print("C is largest")
#             else:
#                 print("D is largest")
#         else:
#             if b>d:
#                 print("B is largest")
# else:
#     if b>c:        
#         if b>d:
#             print("B is largest")
#         else:
#             print("D is largest")
#     else:
#         if c>d:
#             print("C is largest")

# print("enter 1 to +")
# print("enter 2 to -")
# print("enter 3 to *")
# print("enter 4 to /")

# opreater = int(input("\nEnter the opreater ('+','-','*','/') : "))

# num1= int(input("\n\nEnter the number 1 to add : "))
# num2= int(input("Enter the number 2 to add : "))


# match opreater:
#     case 1:
#         print(num1 + num2)
#     case 2:
#         print(num1 - num2)
#     case 3:
#         print(num1 * num2)
#     case 4 :
#         print(num1 /num2)
#     case _:
#         print("invalid")

print("\nenter 1 to buy pizza")
print("enter 2 to buy chips")
print("enter 3 to buy burger")
print("enter 4 to buy sandwich")

# sub_choice=0
# sub_choice1=0
# sub_choice2=0
# sub_choice3=0

choice = int(input("\n\nEnter the choice number : "))

match choice:
    case 1:
        print("\n\nEnter 1 to buy cheese pizza ")
        print("Enter 2 to buy maxicon pizza ")
        print("Enter 3 to buy americon pizza ")

        sub_choice= int (input("\nenter the number to buy :"))

            
        match sub_choice:
            case 1:
                print("\nYou order the cheese pizza")
            case 2:
                print("\nYou order the maxicon pizza ")
            case 3:
                print("\nYou order the americon pizza")
            case _:
                print("invalid")

    case 2:
        print("\nEnter 1 to buy potato chips")
        print("Enter 2 to buy  banana chips")
        print("Enter 3 to buy cheese potato chips ")

        sub_choice1= int (input("\nenter the number to buy :"))
        
        match sub_choice1:
            case 1:
                print("\nYou order the potato chips")
            case 2:
                print("\nYou order the banana chips ")
            case 3:
                print("\nYou order the cheese potato chips")
            case _:
                print("invalid")
        
    case 3:
        print("\nEnter 1 to buy veg burger ")
        print("Enter 2 to buy aloo tiki burger ")
        print("Enter 3 to buy cheese non veg burger ")

        sub_choice2= int (input("\nenter the number to buy :"))
        
        match sub_choice2:
            case 1:
                print("\nYou order the veg burger")
            case 2:
                print("\nYou order the aloo tiki burger ")
            case 3:
                print("\nYou order the cheese non veg burger")
            case _:
                print("invalid")
    case 4:
        print("\nEnter 1 to buy cheese sandwich")
        print("Enter 2 to buy cheese garlic sandwich ")
        print("Enter 3 to buy cheese pienapeal sandwich ")

        sub_choice3= int (input("\nenter the number to buy :"))
        
        match sub_choice3:
            case 1:
                print("\nYou order the cheese sandwich")
            case 2:
                print("\nYou order the cheese garlic sandwich")
            case 3:
                print("\nYou order the cheese pienapeal sandwich")
            case _:
                print("invalid")

    case _:
        print("Invalid")
        


# match sub_choice:
#     case 1:
#         print("\nYou order the cheese pizza")
#     case 2:
#         print("\nYou order the maxicon pizza ")
#     case 3:
#         print("\nYou order the americon pizza")
#     case _:
#         print("invalid")

# match sub_choice1:
#     case 1:
#         print("\nYou order the potato chips")
#     case 2:
#         print("\nYou order the banana chips ")
#     case 3:
#         print("\nYou order the cheese potato chips")
#     case _:
#         print("invalid")

                
# match sub_choice2:
#     case 1:
#         print("\nYou order the veg burger")
#     case 2:
#         print("\nYou order the aloo tiki burger ")
#     case 3:
#         print("\nYou order the cheese non veg burger")
#     case _:
#         print("invalid")

# match sub_choice3:
#     case 1:
#         print("\nYou order the cheese sandwich")
#     case 2:
#         print("\nYou order the cheese garlic sandwich")
#     case 3:
#         print("\nYou order the cheese pienapeal sandwich")
#     case _:
#         print("invalid")
       
                
                
