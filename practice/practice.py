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





# li=[]


# print("\nWelcome to our programme\n")

# print('''Selcet a opition 
# Enter 1 to create a list
# Enter 2 to read a list
# Enter 3 to update the elements of the list
# Enter 4 to delete the elements of the list
# Enter 0 to exit
# ''')

# while True:

#     opition=int(input("\nEnter the your opition = "))

#     if opition==1:
#         num=int(input('Enter the number to create the list : '))

#         for i in range(num):

#             a=int(input(f"Enter the {i+1} => "))
#             li.append(a)

#         print("\nList is created !")

#     elif opition==2:
#         print()
#         for i in li:
#             print(i,end=" ")
#         print()

#     elif opition==3:
#         idx=int(input("\nEnter the index number : "))
#         val=int(input("Enter the new value : "))
#         if idx>=0 and idx<=len(li):
#             li[idx-1]=val

#             print("\nList is updated !")
        
#         else:
#             print("\nInvalid !")

#     elif opition==4:
            
#         idx=int(input("\nEnter the index number : "))
        
#         if idx>=0 and idx<=len(li):
#             li.pop(idx-1)
    
#             print("\nList of element is deleted !")
        
#         else:
#             print("\nInvalid !")

#     elif opition==0:

#         print("\nProgramme is closed !")
#         break


#     else:
#         print("\nInvalid !")
#         break


# student ={

#     "name" : "Alay",
#     "age" : 18,
#     "gread" :"A"

# }
# student["score"]="Delhi"
# student["age"]="25"
# del student["gread"]

# print(student)

# li=["id","name","e-mail"]
# li2=["101","Alay","alaysakhiya@gmail.com"]

# d={
#     li[0] :li2[0],
#     li[1] :li2[1],
#     li[2] :li2[2],

# }

# print(d)


# a=int("123")
# b=tuple([1,2,3,52,62])
# c=list((62,25,42,95))
# d=dict([(1,'A'), (2,'B')])

# print(a)
# print(b)
# print(c)
# print(d,type(d))std=[



# std=[
#     {"id":101 , "name":"Alay", "score" : 90},
#     {"id":102 , "name":"Avinash", "score" : 65},
#     {"id":103 , "name":"Krish", "score" : 53}
# ]



# for i in std:
#     print(i)

#     avg=sum(i["score"])/len(std["score"]) a   
# print(avg)



# for i in student:
#     print(f"name :",i["name"])
# st={
#     "id":len(student)+1,
#     "name" : input("Enter the new name : "),
#     "age" : int(input("Enter the new age :")),
#     "score" : int(input("Enter the new score : "))
# }

# student.append(st)


# for st in student:
#     print(st)



# id=int(input("Enter the id number to update the score : "))
# up_score=int(input("Enter the new score :"))

# found=False

# for i in student:
#     if student[""]==id:
#         student["score"]==up_score
#         found=True
#         print(student)


# update_id = int(input("\nEnter Student ID to Update Score: "))
# new_score = int(input("Enter New Score: "))

# found = False
# for student in student:
#     if student["id"] == update_id:
#         student["score"] = new_score
#         found = True
#         print("Score Updated Successfully!")
#         break

# if not found:
#     print("Student ID not found!")
# print(student)


# name=str(input("Enter the student name to delete : "))
# found=False


# for i in student:
#     if i["Name"]==name:
#         found=True
#         student.remove(i)
# #         print(student)
# found=False
# for i in student:
#     if int(i ["score"])>=80:
#         print(i["Name"])
#         found=True

# student=[

#     {"id" : 1, "Name" : "Alay", "age" :19, "score" : "90"},
#     {"id" : 2, "Name" : "Avinash", "age" :23, "score" : "99"},
#     {"id" : 3, "Name" : "krish", "age" :26 , "score" : "3"}
# ]

# Acount=0
# Bcount=0
# Ccount=0
# Fcount=0

# for i in student:
#     score=int(int(i["score"]))

#     if score>=90:
#         i[ "Grade"]='A'
#         Acount+=1

#     elif score>=80 and score<= 89:
#         i["Grade"]='B'
#         Bcount+=1

#     elif score>=79:
#         i["Grade"]='C'
#         Ccount+=1

#     else:
#         i["Grade"]='F'
#         Fcount+=1

#     print(f"Name :{i["Name"]} | SCORE : {i["score"]} | Grade :{i["Grade"]} ")


# print(f"{Acount} student get A grade")
# print(f"{Bcount} student get B gradeef")
# print(f"{Ccount} student get C grade")
# print(f"{Fcount} student get F grade")


# def greet(name):
#     print("Hello ," +  name)


# greet("Alice")

# def greet(a,b):
#     return a-b

# result=greet(10,5)

# print(result)    


# def pi():
#     return 22/7   

# val=pi()

# print(val)



# mass=int(input("Enter the weight (kg) : "))

# hight=int(input("Enter the hight (in meter) : "))

# hight= hight**2


# bmi=mass/hight

# print("Your BMI is : ",bmi)


# pesos=int(input("Enter the Pesos the left : "))
# soles=int(input("Enter the Soles the left : "))
# reais=int(input("Enter the Reais the left : "))

# pesos=pesos**0.027
# soles=soles**27.93
# reais=reais**18.31

# rupee= (pesos + soles + reais)

# print("\nYour rupees is : ",rupee)
# butterflies = 10
# beetles = 12
# ladybugs = 20

# total=butterflies +beetles +ladybugs 

# print('I caught ' + str(butterflies) + ' 🦋 butterflies!')
# print('I caught ' + str(beetles) + ' 🪲 beetles!')
# print('I caught ' + str(ladybugs) + ' 🐞 ladybugs!')

# print('I caught ' + str(total) + ' total bugs!')

# def add(a, b):
#     '''my NAme is Alay'''
#     print(a+b)
#     return a+b

# print(add.__doc__)

# add(65,235)


# class student:
#     '''writter student age and name'''

#     def name():
#         '''initialise the student age and name'''

# print(student.__doc__)

# print(student.name.__doc__)


# """
# operaters   
# """

# def add(a,b):
#     """return the sum of number"""
#     return a+b

# print(add.__doc__)

# def greet(name):
#     """
#     This funcation greet the person
    
#     Perameter:
#                 name(str) : the name of the person 
                
#     Return :
#                 str :greeting message 
                           
#                    """
#     return f"Hello {name}"

# print(greet.__doc__)


# greet("alay")

# def fact(n):
#     if n==1:
#         return 1
#     elif n<=0:
#         return 0
#     else:
#         return fact(n-1) + fact(n-2)

# print(fact(35))    


# def sum(n):

#     if n==1:
#         return 1
#     else:
#         return n +sum(n-1)
    

# for n in range(1,11):
#     print(sum(n))


# add = lambda a,b,c,d : (a+b)- (c/d)+(a+b+c+d)

# print(add(10,5,90,30))

# num=[52,42,6,9]

# dou=list(filter(lambda n:n%3==0,num))

# print(dou)

# student=[("alay",18),("avi",35),("kri",25),("weg",21)]

# sor=sorted(student,key=lambda x:x[1])

# print(sor)
# sdnvlsd
# set

# defbdbd
# __build_class__

# arr=[
# [46,6,6,1,548,32,65,],
# [46,6,6,1,5,32,65,]
# ]

# print(arr[1])

# arr=[]
# total=0
# largest=0


# num=int(input("Enter the number to add element of the array : "))

# for i in range(num):
#     ele=int(input(f"Enter the no.{i+1} element : "))
#     arr.append(ele)

# for i in arr:
#     if i%2==0:
#         print(i,"is Even")
#     else:
#         print(i,"is Odd")

# print(arr[::-1])

# Check=int(input("Enter the element : "))
# if Check==ele:
#         print("Element is exits !")
# else:
#         print("elemnt is not exits ! ")

# count=int(input("Enter the number to count => "))

# frequency={}
# for i in arr:
#     if i in frequency:
#                 frequency[i]+=1
#     else:
#                 frequency[i]=1

# for key,value in frequency.items():
#         print(f"{key} is {value} times in array")


# num=[51,52,2,1,6,56]

# n=list(filter(lambda i :i>23,num))

# print(num)
# print(n)


li=[]

def data():
    li=list([int(i) for i in input("Enter the number sep by spaces : ").split(" ")])
    print(li)
    return li


li=data()
# def summary(li):
    
#     print(f"""Data Summary : 
#     -Toatal Elements : {len(li)}
#     -Minimum value : {min(li)}  
#     -Maximum value : {max(li)}  
#     -Sum of all value : {sum(li)}
#     -Average value : {sum(li)/len(li)}""")


# summary(li)


def factorial(n):
    
    if n==1:
        return 1
    return n*factorial(n-1)

n=int(input("Enter the number to calculate factorial => "))

print(factorial(n))



        # Threshold 

def threshold():

    val=int(input("Enter the value to filter out data => : "))
            
    filter_from=list(filter(lambda x : x>=val,li ))

    print(filter_from)     


threshold()      



