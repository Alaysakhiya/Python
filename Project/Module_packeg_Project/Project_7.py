from package import Date_time,File_operate,Mathamatic,Random
import uuid

print("""
==========================
Welcome to Multi-utility Toolkit
==========================
""")

while True:

    print("""Choose an opition:
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
            Mathamatic.math.code()
            
    elif choise == 3:
            Random.random.code()

    elif choise == 4:
            print("\nGenerate Unique Indentifier:")
            print(f"Generated UUID :> {uuid.uuid4()}")

    elif choise == 5:
        File_operate.File.code()

    elif choise == 6:
        pass

    elif choise == 7:
        print("Thank you !")
        break

    else:
        print("Invalid Choice !")