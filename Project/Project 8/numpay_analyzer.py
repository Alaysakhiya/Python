import numpy as np 

print("Welcome to the Numpy Analyzer !")

class Array():
    def create(self):
        def __init__(self):
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
        
                else:
                    print("Invalid Choice !")
        
    def array_op(self):
        print("Choice an Operation :")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Back")

class DataAnalytics():
    pass
    

print("""============================
Choose a Opition :
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort , or Filter Array
5. Compute Aggregates and Statistics
6. Exit
""")