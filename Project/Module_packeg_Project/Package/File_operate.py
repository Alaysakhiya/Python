class File():
    def code():

        while True:

            print("""File Operation :
            1. Creat a New File
            2. Write to a File
            3. Read from a File
            4. Append to a File
            5. Back to Main Manu
            """)

            choice = int(input("Enter your Choice :> "))

            if choice == 1:

                name = input("\nEnter File Name (.txt) :> ")
                path = f"D:\\Python\\Project\\Module_packeg_Project\\{name}"

                with open(f"{path}","x") as file :
                    pass
                print("File Created Successfully !")

            elif choice == 2:

                name = input("Enter File Name (.txt) :> ")
                path = f"D:\\Python\\Project\\Module_packeg_Project\\{name}"

                data = input("Enter the Data to Write :> ")
                with open(f"{path}","a") as file:
                    file.write(data)
                    file.write("\n")
                print("Data Added Successfully !")

            elif choice == 3:
                
                name = input("Enter File Name (.txt) :> ")
                path = f"D:\\Python\\Project\\Module_packeg_Project\\{name}"

                with open(f"{path}") as file:
                    file.seek=0
                    print("File Content:")
                    print(file.read())
            

                
            elif choice == 4:
                
                name = input("Enter File Name (.txt) :> ")
                path = f"D:\\Python\\Project\\Module_packeg_Project\\{name}"

                data = input("Enter the Data to Write :> ")
                with open(f"{path}","a") as file:
                    file.write(data)
                    file.write("\n")
                print("Data Added Successfully !")

            elif choice == 5:
                print("Return To The Main Manu")
                break
            else:
                print("Invalid !")
            