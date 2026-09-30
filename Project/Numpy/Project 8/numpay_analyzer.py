import numpy as np 

class ValidELement(Exception):
    pass

print("\n\tWelcome to the Numpy Analyzer !")

class Array():

    def __init__(self):
        self.a1 = None

    def create(self):
                global row1,col1

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
                        row1 = int(input("\nEnter the number of Row :> "))
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

            if self.a1 is None:
                print("Please Create Array First !")
            
            elif self.a1.ndim ==1:
                print("\nOriginal Array :")
                print(self.a1)

                inde = int(input("\nEnter the Index Number:> "))

                print("\nIndex Value of Array ")
                print(self.a1[inde])

            elif self.a1.ndim == 2:
                print("\nOriginal Array :")
                print(self.a1)

                rinde = int(input("\nEnter the Raw Index :> "))
                colinde = int(input("Enter the Column Index :> "))

                print("\nIndex Value of Array ")
                print(self.a1[rinde,colinde])

    def slicing(self):

        if self.a1 is None:
                print("Please Create Array First !")

        elif self.a1.ndim==1:
            print("\nOriginal Array :")
            print(self.a1)

            start = int(input("\nEnter the Start Renge :> "))
            end = int(input("Enter the End Renge :> "))

            print("Slicing Array :")
            print(self.a1[start:end])

        elif self.a1.ndim == 2 :

            print("\nOriginal Array :")
            print(self.a1)

            rstart = int(input("\nEnter the Start Renge of Row :> "))
            rend = int(input("Enter the End Renge of Row :> "))

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
            sub_ch = int(input("\nEnter the Choice :> "))
            try:
                if sub_ch==1:
                    self.indexing()

                elif sub_ch == 2:
                    self.slicing()

                elif sub_ch == 3:
                    print("\nBack to Main Manu")
                    break
                else:
                    print("Invalid Choice !")

            except (ValueError,IndexError):
                raise (ValidELement("Enter Valid Value !"))
            



class DataAnalytics(Array):

    def mathematical(self):
        
        print("\nChoose a Mathematical Operation :")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        sub_c = int(input("\nEnter your Choice :> "))

                    #   Addition

        if sub_c == 1:

            if self.a1 is None:
                print("Please Create Array First !")

            elif self.a1.ndim == 1:
                print("\nOriginal Array :")
                print(self.a1)

                self.addi_ele1 = input("\nEnter the Element of the array separated by space :> ")
                self.addi_a1= np.array(list(map(int,self.addi_ele1.split())))

                print("\nSecond Array !")
                print(self.addi_a1)

                self.result = self.a1 + self.addi_a1
                print("\nResult of Addition :")
                print(self.result)

            elif self.a1.ndim == 2:

                print("\nOriginal Array :")
                print(self.a1)


                self.ele2 = input(f"\nEnter {row1 * col1} elements for the array separated bt space :> ")
                self.addi_a1 = np.array(list(map(int,self.ele2.split()))).reshape(row1,col1)
                print("\nSecond Array !")
                print(self.addi_a1)

                self.result = self.a1 + self.addi_a1

                print("\nResult Of Addition :")
                print(self.result)

                #  Subtraction 

        elif sub_c == 2:

            if self.a1 is None:
                print("Please Create Array First !")

            elif self.a1.ndim == 1:
                print("\nOriginal Array :")
                print(self.a1)

                self.subt_ele1 = input("\nEnter the Element of the array separated by space :> ")
                self.subt_a1= np.array(list(map(int,self.subt_ele1.split())))

                print("\nSecond Array !")
                print(self.subt_a1)

                self.result = self.a1 - self.subt_a1
                print("\nResult of Subtration :")
                print(self.result)

            elif self.a1.ndim == 2:

                print("\nOriginal Array :")
                print(self.a1)


                self.ele2 = input(f"\nEnter {row1 * col1} elements for the array separated bt space :> ")
                self.subt_a1 = np.array(list(map(int,self.ele2.split()))).reshape(row1,col1)
                print("\nSecond Array !")
                print(self.subt_a1)

                self.result = self.a1 - self.subt_a1

                print("\nResult Of Subtration :")
                print(self.result)

                #   Multipilcation 

        elif sub_c == 3:

            if self.a1 is None:
                print("Please Create Array First !")

            elif self.a1.ndim == 1:
                print("\nOriginal Array :")
                print(self.a1)

                self.multi_ele1 = input("\nEnter the Element of the array separated by space :> ")
                self.multi_a1= np.array(list(map(int,self.multi_ele1.split())))

                print("\nSecond Array !")
                print(self.multi_a1)

                self.result = self.a1 * self.multi_a1
                print("\nResult of Multiplication :")
                print(self.result)

            elif self.a1.ndim == 2:

                print("\nOriginal Array :")
                print(self.a1)


                self.multi_ele2 = input(f"\nEnter {row1 * col1} elements for the array separated bt space :> ")
                self.multi_a1 = np.array(list(map(int,self.multi_ele2.split()))).reshape(row1,col1)
                print("\nSecond Array !")
                print(self.multi_a1)

                self.result = self.a1 * self.multi_a1

                print("\nResult Of Multiplication :")
                print(self.result)

                    #  Division

        elif sub_c == 4:
            if self.a1 is None:
                print("Please Create Array First !")

            elif self.a1.ndim == 1:
                print("\nOriginal Array :")
                print(self.a1)

                self.divi_ele1 = input("\nEnter the Element of the array separated by space :> ")
                self.divi_a1= np.array(list(map(int,self.divi_ele1.split())))

                print("\nSecond Array !")
                print(self.divi_a1)

                self.result = self.a1 / self.divi_a1
                print("\nResult of Division :")
                print(self.result)

            elif self.a1.ndim == 2:

                print("Original Array :")
                print(self.a1)


                self.ele2 = input(f"\nEnter {row1 * col1} elements for the array separated bt space :> ")
                self.divi_a1 = np.array(list(map(int,self.ele2.split()))).reshape(row1,col1)
                print("\nSecond Array !")
                print(self.divi_a1)

                self.result = self.a1 / self.divi_a1

                print("\nResult Of Division :")
                print(self.result)
        else:
            print("\nInvalid Choice !")

    def combi_spli(self):

        print("\nChoose an opition :")
        print("1. Combine Array")
        print("2. Split Array")

        sub_choice = int(input("\nEnter your Choice :> "))

        if sub_choice == 1:

            if self.a1 is None :
                print("Please Create Array First !")

            elif self.a1.ndim == 1:

                data = input("\nEnter the Element of the array separated by space :> ")
                arr = np.array(list(map(int,data.split())))

                print("\nOriginal Array :")
                print(self.a1)

                print("\nSecond Array :")
                print(arr)

                print("\nCombined Array ( Vertical Stack ) : ")
                print(np.concat((self.a1,arr)))

            elif self.a1.ndim == 2:

                data = input(f"\nEnter {row1 * col1} elements for the array separated bt space :> ")
                arr =  np.array(list(map(int,data.split()))).reshape(row1,col1)

                print("\nOriginal Array :")
                print(self.a1)

                print("\nSecond Array :")
                print(arr)


                print("\nCombined Array ( Vertical Stack ) : ")
                print(np.concat((self.a1,arr))) 

        elif sub_choice == 2:

            if self.a1 is None :
                print("Please Create Array First !")

            elif self.a1.ndim == 1 :
                
                print("\nOriginal Array :")
                print(self.a1)

                part = int(input("\nEnter Number split in equal part :> "))
                split_arr = np.hsplit(self.a1,part)

                print("\nSplit Array :")
                print(split_arr)

            elif self.a1.ndim == 2:


                print("\nOriginal Array :")
                print(self.a1)

                part = int(input("\nEnter Number split in equal part :> "))
                split_arr = np.vsplit(self.a1,part)

                print("\nSplit Array :")
                print(split_arr)

    def search(self):

        print("\nChoose an Operation")
        print("1. Search a Value")
        print("2. Sort the Array")
        print("3. Filter Value")

        sub_choice = int(input("\nEnter your Choice :> "))



        if sub_choice==1:

            if self.a1 is None :
                print("\nPlease Create Arrat First !")

            elif self.a1.ndim == 1:

                find = int(input("\nEnter Number to Search :> "))
                index = np.where(self.a1 == find)
                print(f"\nIndex of {find} : {index[0]}")

            elif self.a1.ndim == 2:

                find = int(input("\nEnter Number to Search :> "))
                index = np.where(self.a1 == find)
                print(f"\nIndex of {find} : {index}")

        elif sub_choice == 2:

            if self.a1 is None :
                print("\nPlease Create Arrat First !")

            elif self.a1.ndim == 1 or self.a1.ndim == 2:

                sort_arr = np.sort(self.a1)
                print("\nOriginal Array :")
                print(self.a1)


                print("\nSorted Array : ")
                print(sort_arr)

        elif sub_choice == 3:

            print("\n1. Greater Then (>) ")
            print("2. Less Then (<) ")

            s_choice = int(input("\nEnter your Choice :> "))

            if self.a1 is None :
                print("\nPlease Create Arrat First !")

            elif s_choice == 1:

                num = int(input("\nEnter the Number :> "))

                mask = self.a1> num 
                filt_arr = self.a1[mask]

                print("\nOriginal Array :")
                print(self.a1)

                print("\nFilter Array :")
                print(filt_arr)

            elif s_choice == 2:

                num = int(input("\nEnter the Number :> "))

                mask = self.a1 < num 
                filt_arr = self.a1[mask]

                print("\nOriginal Array :")
                print(self.a1)

                print("\nFilter Array :")
                print(filt_arr)

            else:
                print("Invalid Choice !")
        else : 
            print("Invalid Choice !")

    def aggregate(self):
    
            print("\nChoose an Aggregate / Statistical Operatrion :")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")

            sub_choice = int(input("\nEnter your Choice :> "))

            if self.a1 is None :
                print("Please Create Array First !")

            elif sub_choice == 1:
                print("\nOriginal Array :")
                print(self.a1)

                print("\nSum:", np.sum(self.a1))

            elif sub_choice == 2:
                print("\nOriginal Array :")
                print(self.a1)
                print("\nMean:", np.mean(self.a1)) 

            elif sub_choice == 3:

                print("\nOriginal Array :")
                print(self.a1)
                print("\nMedian:", np.median(self.a1)) 

            elif sub_choice == 4:

                print("\nOriginal Array :")
                print(self.a1)
                print("\nStandard Deviation:", np.std(self.a1))

            elif sub_choice == 5:
                print("\nOriginal Array :")
                print(self.a1)
                print("\nVariance:", np .var(self.a1)) 


            else:
                print("Invalid Choice !")


obj1 = DataAnalytics()
while True:
    print("""============================
    Choose a Opition :
    1. Create a Numpy Array
    2. Perform Mathematical Operations
    3. Combine or Split Arrays
    4. Search, Sort , or Filter Array
    5. Compute Aggregates and Statistics
    6. Exit
    """)

    choise = int(input("Enter your Choice :> "))


    try :
        if choise == 1:

            obj1.create()
            obj1.operation()


        elif choise == 2:

            obj1.mathematical()

        elif choise == 3:

            obj1.combi_spli()
        
        elif choise == 4:

            obj1.search()

        elif choise == 5:

            obj1.aggregate()

        elif choise == 6:
            print("\n Thank you for Using Numpy Analyzer ! Goodbye !\n")
            break

        else :
            print("\nInvalid Choice !")

    except (ValueError,ValidELement,IndexError) as er:
            print("Enter Valid Value !")
            print(er)
