import numpy as np 
from abc import abstractmethod

@abstractmethod
class ValidELement(Exception):
    pass

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
                    try:
                        ele2 = input(f"Enter {row1 * col1} elements for the array separated bt space :> ")
                        a2 = np.array(list(map(int,ele2.split()))).reshape(row1,col1)
                        print("Array Created Successfully :")
                        print(a2)
                    except:
                        ValidELement("Enter Valid Element Renge")
            
                else:
                    print("Invalid Choice !")
        
                print("Choice an Operation :")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Back")

                sub_ch = int(input("\nEnter the Choice :>"))

                if sub_ch ==1 :
    
                    if a1.ndim ==1:
                        print("\nOriginal Array :")
                        print(a1)

                        inde = int(input("\nEnter the Index Number:> "))

                        print("\nIndex Value of Array ")
                        print(a1[inde])

                    elif a1.ndim == 2:
                        print("\nOriginal Array :")
                        print(a1)

                        rinde = int(input("Enter the Raw Index :> "))
                        colinde = int(input("Enter the Column Index :> "))

                        print("\nIndex Value of Array ")
                        print(a1[rinde,colinde])

                    



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