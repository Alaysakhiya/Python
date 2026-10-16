import numpy as np
import matplotlib.pyplot as pllt
import seaborn as sb
import pandas as pd





print("\n\t======Welcome to E-Library Data Insights Dashboard======")


class LibraryDashboard:

    def __init__(self):
        self.data = None

    def load_data(self,file_path):
        try:
            
            self.data = pd.read_csv(file_path)
            print("\nDataset Loaded Successfully !")

        except(FileNotFoundError):
            print ("\nFile Not Found Enter Valid File Name")

    def calculate_statistic(self):
        if self.data is None :
            print("\nPlease Load Dataset First !")
            return  

        print("\n\t==Calculate Statistic==")
        print("1. Most Borrowed Book")
        print("2. Average Borrow Time")
        print("3. Busiest Day")

        #  Most borrowed item
        sub_choice = int(input("\nEnter Your Choice :> "))

        if sub_choice == 1:
            count_book = self.data["Book Title"].value_counts()
            print("\n====Most Borrowed Book====")
            print(count_book.idxmax())

        #  Avrage of borrowing
        elif sub_choice == 2:
            avg = self.data["Borrowing Duration (Days)"].to_numpy()
            print("\n====Average Borrow Time====")
            print(np.average(avg))

        # busiest day
        elif sub_choice == 3:
            count_day = self.data["Date"].value_counts()
            print("\n====Busiest Day====")
            print(count_day.idxmax())

        else:
            print("\nInvalid Choice !")

    def filter_transaction(self):
        if self.data is None :
            print("\nPlease Load Dataset First !")
            return  
        
        print("\n\t==Filter==")
        print("1. In Genre")
        print("2. In Borrowing Duration")

        sub_choice = int(input("\nEnter the choice :> "))

        if sub_choice == 1:

            genre = input("\nEnter the Genre of Book :> ")
            genre_filter = self.data[self.data["Genre"] == genre]
            print(f"\nFilter with {genre}")
            print(genre_filter)

        elif sub_choice ==2:

            day = int(input("Enter the Borrowing Duration (Days) :> "))

            print("\n1. In Less Then (<)")
            print("2. In Greater Then (>)")

            sub_c = int(input("\nEnter your Choice :> "))

            if sub_c == 1:
                day_filter = self.data[self.data["Borrowing Duration (Days)"] < day ]
                print("\nFilter in Borrowing Duration with (<)")
                print(day_filter)

            elif sub_c == 2:
                day_filter = self.data[self.data["Borrowing Duration (Days)"] > day ]
                print("\nFilter in Borrowing Duration with (>)")
                print(day_filter)

            else:
                print("\nInvalid Choice !")
        else:
            print("\nInvalid Choice !")

obj = LibraryDashboard()
obj.load_data("D:\\Python\\Project\\Practical_Exam\\library_transaction.csv")
# obj.calculate_statistic()
# obj.filter_transaction()