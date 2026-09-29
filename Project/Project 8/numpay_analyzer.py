import numpy as np 

class ValidELement(Exception):
    pass

print("Welcome to the Numpy Analyzer !")

class Array():
    def create(self):
                print("Select the type of Array to create :>")
                print("1. 1D Array") 
                print("2. 2D Array") 
        
                sub_choice = int(input("\nEnter the Choice :> "))
        
                if sub_choice == 1:
                    ele1 = input("Enter the Element of the array separated by space :> ")
                    
                    self.a1 = np.array(list(map(int,ele1.split())))
                    print("Array Created Successfully :")
                    print(self.a1)
        
                elif sub_choice == 2:

                    try:
                        row1 = int(input("Enter the number of Row :> "))
                        col1 =int(input("Enter the number of Columns :> "))
                        ele2 = input(f"Enter {row1 * col1} elements for the array separated bt space :> ")
                        self.a1 = np.array(list(map(int,ele2.split()))).reshape(row1,col1)
                        print("\nArray Created Successfully :")
                        print(self.a1)

                    except ValueError:

                        raise (ValidELement("Enter Valid Element Renge"))
            
                else:
                    print("Invalid Choice !")
                    
    def indexing(self):
            
            if self.a1.ndim ==1:
                print("\nOriginal Array :")
                print(self.a1)

                inde = int(input("\nEnter the Index Number:> "))

                print("\nIndex Value of Array ")
                print(self.a1[inde])

            elif self.a1.ndim == 2:
                print("\nOriginal Array :")
                print(self.a1)

                rinde = int(input("Enter the Raw Index :> "))
                colinde = int(input("Enter the Column Index :> "))

                print("\nIndex Value of Array ")
                print(self.a1[rinde,colinde])

    def slicing(self):

        if self.a1.ndim==1:
            print("\nOriginal Array :")
            print(self.a1)

            start = int(input("\nEnter the Start Renge :> "))
            end = int(input("Enter the End Renge :> "))

            print("Slicing Array :")
            print(self.a1[start:end])

        elif self.a1.ndim == 2 :

            print("\nOriginal Array :")
            print(self.a1)

            rstart = int(input("\nEnter the Start Renge of Raw :> "))
            rend = int(input("Enter the End Renge of Raw :> "))

            colstart = int(input("\nEnter the Start Renge of Column :> "))
            colend = int(input("Enter the End Renge of Column :> "))

            print("Slicing Array :")
            print(self.a1[rstart:rend,colstart:colend])


    def operation(self):

        while True:    
            print("\nChoice an Operation :")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Back")
            sub_ch = int(input("\nEnter the Choice :>"))
            try:
                if sub_ch==1:
                    self.indexing()

                elif sub_ch == 2:
                    self.slicing()

                elif sub_ch == 3:
                    print("Back to Main Manu")
                    break
                else:
                    print("Invalid Choice !")

            except (ValueError,IndexError):
                raise (ValidELement("Enter Valid Value !"))
            



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