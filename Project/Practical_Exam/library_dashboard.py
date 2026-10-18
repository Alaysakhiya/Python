import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import datetime





print("\n\t======Welcome to E-Library Data Insights Dashboard======")


class LibraryDashboard:

    def load_data(self,file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("\nDataset Loaded Successfully !")
            
            

        except(FileNotFoundError):
            print ("\nFile Not Found Enter Valid File Name")

    def calculate_statistic(self):


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
        
        
        print("\n\t==Filter==")
        print("1. In Genre")
        print("2. In Borrowing Duration")

        sub_choice = int(input("\nEnter the choice :> "))

        if sub_choice == 1:

            genre = input("\nEnter the Genre of Book :> ")
            genre_filter = self.data[self.data["Genre"].astype(str).str.casefold() == genre.casefold()]
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

    def generate_report(self):

        print("\n----Generate Report----")
        print("1. Calculate Borrowing Statistics")
        print("2. Grouping Book by Genre")
        print("3. Aggregating Metrics")

        sub_choice = int(input("\nEnter your Choice :> "))

        if sub_choice == 1:
            print("\n1. Maximum Time")
            print("2. Standard Deviation")
            print("3. Median")
            print("4. Total Borrowing Time")

            sub_c = int(input("\nEnter Your Choice :> "))

            if sub_c == 1:
                max_time=self.data["Borrowing Duration (Days)"].max()
                print(f"\nMaximum Duration For Borrowing Book :> {max_time}")

            elif sub_c == 2:

                day = self.data["Borrowing Duration (Days)"]
                std= np.std(day)
                print("\nStandard Deviation")
                print(std)

            elif sub_c == 3:
                day = self.data["Borrowing Duration (Days)"]
                day_median = np.median(day)
                print(f"\nMedian of Borrowing Duration :> {day_median}")

            elif sub_c == 4:
                day = self.data["Borrowing Duration (Days)"]
                print(f"\nTotal Borrowing Time :> {np.sum(day)} Day")

            else:
                print("\nInvalid Choice !")

        elif sub_choice == 2:

            group = self.data.groupby("Genre")

            summary = group.agg(
                Total_Borrowing=("Book Title","count"),
                Average_Time = ("Borrowing Duration (Days)","mean"),
                Total_Day=("Borrowing Duration (Days)","sum"))

            print("\n----Group By Book Genre----\n")
            print(summary)

        elif sub_choice == 3:

            print("\n----Total Borrowing By Book----\n")
            by_book = self.data.groupby("Book Title")["Borrowing Duration (Days)"].agg("count")
            print(by_book)

        else:
            print("\nInvalid Choice !")

    def data_visulation(self):
        while True:
            print("\n\t-----Data Visulation-----")
            print("1. Bar Chart")
            print("2. Line Chart")
            print("3. Pie Chart")
            print("4. Heatmap")
            print("5. Back to Main Manu")

            sub_choice = int(input("Enter Your Choice :> "))

            if sub_choice == 1:
                x = self.data["Book Title"].value_counts().head(5)
                print("\n-----Bar Chart-----")
                plt.figure(figsize=(7,4))
                sb.barplot(x=x.index,y=x)
                plt.xticks(fontsize = 5)
                plt.xlabel("Book Title")
                plt.ylabel("Count")
                plt.show()
                print("Bar Chart Succesfully Display !")

            elif sub_choice == 2:
                x=[]
                self.data["Date"]= pd.to_datetime(self.data["Date"])
                
                for i in self.data["Date"]:
                    date =datetime.datetime.strftime(i,"%Y-%m")
                    x.append(date)

                print("\n----Line Chart-----")
                plt.figure(figsize=(10,5))
                sb.lineplot(data=self.data,x=x,y="Borrowing Duration (Days)")
                plt.xticks(fontsize = 6)
                plt.xlabel("Month")
                plt.ylabel("Borrowing Duration (Days)")
                plt.show()

            elif sub_choice == 3:
                a1= self.data["Genre"].value_counts()

                print("\n-----Pie Chart-----")
                plt.pie(a1.values,labels=a1.index)
                plt.title("Pie Chart")
    
                plt.show()
                print("Pie Chart Display Successfully !")

            elif sub_choice == 4:
            
                print("\n-----Heatmap-----")
                pivot_data = self.data.pivot_table(
                    index="Genre", columns="Borrowing Duration (Days)",values="Date",aggfunc="count"
                )

                plt.figure(figsize=(8,5))
                sb.heatmap(pivot_data,cmap="Reds",annot=True,annot_kws={"size" : 5})
                plt.show()
                print("\nHeatmap Display Successfully !")

            elif sub_choice == 5:
                print("\nBack to Main Menu")
                break

            else:
                print("\nInvalid Choice !")

obj = None
while True:
    print("\nPlease Select a Opition :>")
    print("1. Load Dataset")
    print("2. Claculate Statistic")
    print("3. Filter")
    print("4. Summary Report")
    print("5. Data Visulation")
    print("6. Exit\n")

    try:
        choice = int(input("Enter your Choice :> "))

        if choice == 1:
            obj = LibraryDashboard()
            obj.load_data("library_transaction.csv")

        elif choice == 2:
            if obj is None:
                print("\nPlease Load Dataset First !!")
            
            else:
                obj.calculate_statistic()

        elif choice == 3:
            if obj is None:
                print("\nPlease Load Dataset First !!")
            else:
                obj.filter_transaction()

        elif choice == 4:
            if obj is None:
                print("\nPlease Load Dataset First !!")
            else:
                obj.generate_report()

        elif choice == 5:
            if obj is None:
                print("\nPlease Load Dataset First !!")

            else:
                obj.data_visulation()

        elif choice == 6:
            print("\nThank You For Visiting ")
            break

        else:
            print("\nInvalid Choice")

    except(ValueError):
        print("Enter Valid Value !")
