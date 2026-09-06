from datetime import datetime


print("\t=====Welcome to Personal Journal Manager !=====")

class ChoiceError(Exception):
    pass
class NoEntryError(Exception):
    pass

class Journal():

    def entry(self):

        data = input("Enter your Entry Here :> ")
        a=datetime.now()
        with open("D:\\Python\\Project\\File_project\\Journal.txt","a") as file :
            file.write(f"\n[{str(a)}]\n{data}\n\n")

    def view(self):

        with open("D:\\Python\\Project\\File_project\\Journal.txt") as file:
            Entry = file.read()
            if len(Entry) == 0:
                    raise NoEntryError("\nThere are No entry in File ")
            print(Entry)

    def search(self):

        with open("D:\\Python\\Project\\File_project\\Journal.txt") as file:
            keyword = input("Enter Keyword to find Entry :> ")
            found = False
            data = file.read().strip().split("\n\n")
            for i in data:
                if keyword.lower() in i.lower():
                    found = True
                    print(i)
                

            if not found:
                raise NoEntryError("No Entry Found !")

    def delete_Entry(self):
        sub_choice = input("Are you sure you want to Delete all Entries ? (yes or no) :> ")

        if sub_choice.lower() == "yes":

            with open("D:\\Python\\Project\\File_project\\Journal.txt","w") as file:
                file.write("")
            print("All Entry are Deleted !")
            

        elif sub_choice.lower() == "no":
            print("All entries will not be Delete !")

        else:
            raise ChoiceError("\n Enter valid Choice !")



Journal_Management = Journal()

while True :
    print("""
Please Select the choice :>

    1. To Add a New Entry
    2. To View All Entry
    3. To Search for an Entry
    4. To Delete All Entries
    5. Exit

""")
    try:
        choice= int (input("Enter the your Choice :> "))

    except ValueError as e:
        print("Enter the valid Choice !")
        continue

    if choice==1 :

        try:
            Journal_Management.entry()
            print("Your Entry is Added Successfully ")
        except FileNotFoundError as a:
            print(a)


    elif choice == 2:
        try:
            Journal_Management.view()
        except (NoEntryError,FileNotFoundError) as a:
            print(a)

    elif choice == 3:
        try:
            Journal_Management.search()
        except (NoEntryError,FileNotFoundError) as a:
            print(a)

    elif choice == 4 :

        try:
            Journal_Management.delete_Entry()
        except ChoiceError as a:
            print(a)

    elif choice == 5:

        print("Thank you for visiting Jounral Management !")
        break

    else:

            try:
                raise ChoiceError("\nEnter the Valid Chocice !")
            except ChoiceError as a:
                print(a)


