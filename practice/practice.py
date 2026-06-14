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

# print("\nenter 1 to buy pizza")
# print("enter 2 to buy chips")
# print("enter 3 to buy burger")
# print("enter 4 to buy sandwich")



# choice = int(input("\n\nEnter the choice number : "))

# match choice:
#     case 1:
#         print("\n\nEnter 1 to buy cheese pizza ")
#         print("Enter 2 to buy maxicon pizza ")
#         print("Enter 3 to buy americon pizza ")

#         sub_choice= int (input("\nenter the number to buy :"))

            
#         match sub_choice:
#             case 1:
#                 print("\nYou order the cheese pizza")
#             case 2:
#                 print("\nYou order the maxicon pizza ")
#             case 3:
#                 print("\nYou order the americon pizza")
#             case _:
#                 print("invalid")

#     case 2:
#         print("\nEnter 1 to buy potato chips")
#         print("Enter 2 to buy  banana chips")
#         print("Enter 3 to buy cheese potato chips ")

#         sub_choice1= int (input("\nenter the number to buy :"))
        
#         match sub_choice1:
#             case 1:
#                 print("\nYou order the potato chips")
#             case 2:
#                 print("\nYou order the banana chips ")
#             case 3:
#                 print("\nYou order the cheese potato chips")
#             case _:
#                 print("invalid")
        
#     case 3:
#         print("\nEnter 1 to buy veg burger ")
#         print("Enter 2 to buy aloo tiki burger ")
#         print("Enter 3 to buy cheese non veg burger ")

#         sub_choice2= int (input("\nenter the number to buy :"))
        
#         match sub_choice2:
#             case 1:
#                 print("\nYou order the veg burger")
#             case 2:
#                 print("\nYou order the aloo tiki burger ")
#             case 3:
#                 print("\nYou order the cheese non veg burger")
#             case _:
#                 print("invalid")
#     case 4:
#         print("\nEnter 1 to buy cheese sandwich")
#         print("Enter 2 to buy cheese garlic sandwich ")
#         print("Enter 3 to buy cheese pienapeal sandwich ")

#         sub_choice3= int (input("\nenter the number to buy :"))
        
#         match sub_choice3:
#             case 1:
#                 print("\nYou order the cheese sandwich")
#             case 2:
#                 print("\nYou order the cheese garlic sandwich")
#             case 3:
#                 print("\nYou order the cheese pienapeal sandwich")
#             case _:
#                 print("invalid")

#     case _:
#         print("Invalid")
        


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
#                 
                
# while True:
#     num=int(input("enter the 0 to exit :"))
#     if num==0:
#         break

# for i in range(0,10):
#     print(i+1 ,"X",i+1,"=",(i+1)*(i+1))

# i=0


# while i<51:

#     i+=1
#     if i%2==0:
#         print(i,"Number is even")
#     # else:
#     #     print(i,"Number is Odd")
    

# for i in range (1,20):
#     if i%2==0:
#         print()
#     else:
#         print(i,"number is Odd")


# for i in range(1,50):
#     if i%2==0:
#         print(i, "\nNumber is divided by 2")
#     elif i%3==0:
#         print(i ,"\nNumber is divided by 3")
#     else:
#         print(i ,"Number is divided by both")

#         lab 2.4




# for i in range(1,20):
#     if i%4==0:
#         continue
#     print(i)



# while True:

#     num=int(input("Enter the number(1 to 10) : "))

#     if num==7:
#         break
#     else:
#         print("Your number is ",num)



# name=str(input("Enter the name :"))

# for vowel in name:
#     if vowel in "AEIOUaeiou":
#         continue
#     print(vowel,end=" ")

# tabel=int(input("\nEnter the tabel :"))

# for i in range(tabel,tabel+1):
#     for j in range(1,11):
#         print(i,"X",j,"=",i*j)

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" " )
#     print()

# for i in range(5,0,-1):
#     for j in range(i,6,):
#         print(j,end=" ")
#     print()

# a ="alay sakhiya"
# b="sakhiya"


# print(a.replace("alay" ,"hello"))





li=[]


print("\nWelcome to our programme\n")

print('''Selcet a opition 
Enter 1 to create a list
Enter 2 to read a list
Enter 3 to update the elements of the list
Enter 4 to delete the elements of the list
Enter 0 to exit
''')

while True:

    opition=int(input("\nEnter the your opition = "))

    if opition==1:
        num=int(input('Enter the number to create the list : '))

        for i in range(num):

            a=int(input(f"Enter the {i+1} => "))
            li.append(a)

        print("\nList is created !")

    elif opition==2:
        print()
        for i in li:
            print(i,end=" ")
        print()

    elif opition==3:
        idx=int(input("\nEnter the index number : "))
        val=int(input("Enter the new value : "))
        if idx>=0 and idx<=len(li):
            li[idx-1]=val

            print("\nList is updated !")
        
        else:
            print("\nInvalid !")

    elif opition==4:
            
        idx=int(input("\nEnter the index number : "))
        
        if idx>=0 and idx<=len(li):
            li.pop(idx-1)
    
            print("\nList of element is deleted !")
        
        else:
            print("\nInvalid !")

    elif opition==0:

        print("\nProgramme is closed !")
        break


    else:
        print("\nInvalid !")
        break

