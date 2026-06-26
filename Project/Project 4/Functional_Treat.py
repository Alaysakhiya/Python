
print("\nWelcome to the Data Analyzer and Transformer Program ")


li=[]


def data():
    global li
    li=list([int(i) for i in input("Enter the number sep by spaces : ").split(" ")])
    print(li) 
    

# displaY Data

def summary(li):
    
    print(f"""Data Summary : 
    -Toatal Elements : {len(li)}
    -Minimum value : {min(li)}  
    -Maximum value : {max(li)}  
    -Sum of all value : {sum(li)}
    -Average value : {sum(li)/len(li)}""")
    



    # Factorial (Recursion)

def factorial(n):
    
    if n==1:
        return 1
    return n*factorial(n-1)
    
    # Threshold

def threshold():

    val=int(input("Enter the value to filter out data => : "))
            
    filter_from=list(filter(lambda x : x>=val,li ))

    print(f"Filtered Data (value >= {val}) :")
    print(filter_from)  


    # Sorting

def sorting():
        
        print('''\n Enter 1 to Accending order
Enter 2 to Descending order''')

        sub_choice=int(input("Enter Sub choice : "))

        if sub_choice==1:
            print(sorted(li))
        
        elif sub_choice==2:
            print(sorted(li,reverse=True,))

        else:
            print("Invalid !")
            

        # Stat dataset

def Stat_data(li):
            
            total=sum(li)
            Maximum=max(li)
            Minimum=min(li)
            Avreage=sum(li)/len(li)
            
            return total,Maximum,Minimum,Avreage


    
def exit():
    print("Thank you for visting Data Analyzer and Transformer Program !")
        


while True:

    print("""
        Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program 
        """)
    

    choice=int(input("Enter the choice = "))

    if choice==1:
        data()
        print("\nData has been stored Successfully !")

    elif choice==2:
        summary(li)

    elif choice==3:
        n=int(input("Enter the number to calculate factorial => "))
    
        print(f"factorial of {n} is",factorial(n))

    elif choice==4:

            threshold()

    elif choice==5:

            sorting()

    elif choice==6:
            display_data=Stat_data(li)
            print(display_data)
    

    elif choice==7:
            exit()
            break
    
    else:
        print("Invalid !")
        break