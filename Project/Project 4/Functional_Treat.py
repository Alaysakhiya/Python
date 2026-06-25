
print("\nWelcome to the Data Analyzer and Transformer Program ")


li=[]


def data():
    global li
    li=list([int(i) for i in input("Enter the number sep by spaces : ").split(" ")])
    print(li) 
    return li

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
    
    n=int(input("Enter the number to calculate factorial => "))
    if n==1:
        return 1
    return n*factorial(n-1)
    
    # Threshold

def threshold():

    val=int(input("Enter the value to filter out data => : "))
            
    filter_from=list(filter(lambda x : x>=val,li ))

    print(f"Filtered Data (value >= {val})",filter_from)  

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

        print(f"factorial of {n} is",factorial(n))

    elif choice==4:

            print(threshold())
