print("\nWelcome to the Interactive Personal Data Collector !\n\n")

name = str(input("Please Enter the your Name : " ))
age = int(input("Please Enter the your Age : "))
height =float(input("Please Enter the your Height (In feet): "))
num =int(input("Please Enter the your Favourite Number : "))
year =int(input("Please Enter the current Year : "))
print("\nThank you ! here the information we have collected\n\n")


print("Name :",name,"(Type : ",type(name),",memory address :",id(name),")")
print("Age :",age,"(Type : ",type(age),",memory address :",id(age),")")
print("Height :",height,"(Type : ",type(height),",memory address :",id(height),")")
print("Favourite number:",num,"(Type : ",type(num),",memory address :",id(num),")")




year= year-age

print("\nYour birth year is approximately :",year,"(based on the your age of ",age,")")


print("\n Thank you for using the personal Data Collecter. Goodbye !")


