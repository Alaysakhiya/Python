print("\nWelcome to the Pattern Generator and Number Analyzer !")


while True:

    print("\nSelect the option: ")
    print(1," To Generate the pattern")
    print(2," To Analyze Range of Number ")
    print(3," To Exit")

    choice=int(input("\nEnter the choice : "))


    match choice:

        case 1:

            print("Enter the 1 to * Pattern")
            print("Enter the 2 to $ pattern")

            sub_choice=int(input("\nEnter the number to sub choice : "))
           
        

            if sub_choice==1:
                row=int(input("\nEnter the number of the Row for pattern : " ))
                for i in range(1,row+1):
                    for j in range(1,i+1):
                        print("*",end=" ")
                    print()  
            elif sub_choice==2:
               row=int(input("\nEnter the number of the Row for pattern : " ))
               for i in range(1,row+1):
                    for j in range(1,i+1):
                        print("$",end=" ")
                    print()  
               else:
                   print("\nInvalid !")
                   
        case 2:

            start=int(input("\nEnter the start of the range : "))
            end=int(input("Enter the end of range : "))   
            total=sum(range(start,end+1))


            if end<start:
                for i in range(start,end,-1):
                    if i%2==0:
                     print(f"\nNumber is {i} Even ")
                    else:
                     print(f"\nNumber is {i} Odd") 
                     total=sum(range(start,end,-1))
            else:
            
             for i in range(start,end+1):
                if i%2==0:
                    print(f"\nNumber is {i} Even ")
                else:
                    print(f"\nNumber is {i} Odd")  
            print("\nSum of all Number betwwen",start,"to",end ,"is:",total)  
        case 3:

            print("\nExiting the program.   Goodbye !")
            
            break



        case _:
            
            print("Invalid !")
            break
                  

