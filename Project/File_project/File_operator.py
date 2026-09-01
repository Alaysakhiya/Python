from datetime import datetime


print("\t=====Welcome to Personal Journal Manager !=====")

class ChoiceError(Exception):
    pass
class NoEntryError(Exception):
    pass
mydata = []

while True :
    print("""
Please Select the choice :>

    1. To Add a New Entry
    2. To View All Entry
    3. To Search for an Entry
    4. To Delete All Entries
    5. Exit

""")

    choice= int (input("Enter the your Choice :> "))

    if choice==1 :

        data = input("Enter your Entry Here :> ")
        with open("D:\\Python\\Project\\File_project\\Journal.txt","a") as file :

            file.write(data)
            file.write("\n")
            mydata.append(datetime.now())
            print(mydata)
            data.split("\n")
            

        print("Your Entry is Added Successfully ")

    elif choice == 2:

        with open("D:\\Python\\Project\\File_project\\Journal.txt") as file:
            Entry = file.read()
            try:
                if len(Entry) == 0:
                    raise NoEntryError("\nThere are No entry in File ")
            except NoEntryError:
                raise
            else:
                print(Entry)

            
            
    elif choice == 3:

        with open("D:\\Python\\Project\\File_project\\Journal.txt") as file:
            pass

    elif choice == 4 :

        sub_choice = input("Are you sure you want to Delete all Entries ? (yes or no) :> ")
        if sub_choice == "yes":
            with open("D:\\Python\\Project\\File_project\\Journal.txt","w") as file:
                file.write("")

        elif sub_choice == "no":
            print("All entries will not be Delete !")

        else:
            try:
                if choice ==" ":
                    raise ChoiceError("\nEnter the Valid Chocice !")
            except ChoiceError :
                raise


    elif choice == 5:

        print("You Successfully Exited !")
        break

    else:
        try:
            raise ChoiceError("\nEnter the Valid Chocice !")
        except ChoiceError:
            raise


