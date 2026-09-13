from package import Date_time,Mathamatic,Random
import uuid
import package

print("""
==========================
Welcome to Multi-utility Toolkit
==========================""")

while True:

        print("""
Choose an opition:
        1. Datetime and Time Operation
        2. Mathematical Operation
        3. Random Data Generation
        4. Generate Unique Identifier (UUID)
        5. File Operation (Custom Module)
        6. Explore Module Attribute (dir())
        7. Exit 
        """)


        choise = int(input("Enter the your Choise :> "))

        if choise == 1:
                Date_time.Datetime.code()

        elif choise == 2:
                Mathamatic.main.code()
                
        elif choise == 3:
                Random.main.code()

        elif choise == 4:
                print("\nGenerate Unique Indentifier:")
                print(f"Generated UUID :> {uuid.uuid4()}")

        elif choise == 5:

                package.File_operate.File.code()

        elif choise == 6:
                print("\nExplore Module Aatribute :")
                name = input("Enter Module Name to Explore :> ").lower()

                module ={
                        "datetime" : Date_time,
                        "file_operate" : package.File_operate,
                        "random" : Random,
                        "uuid" : uuid,
                        "math" : Mathamatic,
                        "package" : package
                }
                if name in module:
                        print(f"\nAvailable Attributes in {name} Module :")
                        print(dir(module[name]))
                else:
                        print("Module not Found !")
        elif choise == 7:

                print("Thank you for using the Multi-Utility Toolkit !")
                break

        else:
                print("Invalid Choice !")