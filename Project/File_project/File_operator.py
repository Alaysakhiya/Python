from datetime import datetime


print("\n\t=====Welcome to Personal Journal Manager !=====")

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
        try:
            with open("D:\\Python\\Project\\File_project\\Journal.txt") as file:
                Entry = file.read()
                if len(Entry) == 0:
                        raise NoEntryError("\nThere are No entry in File ")
                print(Entry)
                
        except FileNotFoundError:
            raise FileNotFoundError("Journal file not be Found ")

    def search(self):
        try:
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
        except FileNotFoundError:
            raise FileNotFoundError("Journal File not be Found !")

    def delete_Entry(self):
        try:
            sub_choice = input("Are you sure you want to Delete all Entries ? (yes or no) :> ")

            if sub_choice.lower() == "yes":

                with open("D:\\Python\\Project\\File_project\\Journal.txt","w") as file:
                    file.write("")
                print("All Entry are Deleted !")
                

            elif sub_choice.lower() == "no":
                print("All entries will not be Delete !")

            else:
                raise ChoiceError("\nEnter valid Choice !")
        except FileNotFoundError:
            raise FileNotFoundError("Journal file not be Found !")



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
    choice= int (input("Enter the your Choice :> "))


    try:
        if choice==1 :

                Journal_Management.entry()
                print("Your Entry is Added Successfully ")


        elif choice == 2:
                Journal_Management.view()

        elif choice == 3:
                
                Journal_Management.search()

        elif choice == 4 :

                Journal_Management.delete_Entry()
                
        elif choice == 5:

            print("Thank you for visiting Jounral Management !")
            break

        else:
            raise ChoiceError("\nEnter the Valid Chocice !")

    except(ChoiceError,FileNotFoundError,NoEntryError) as a:
        print(a)


