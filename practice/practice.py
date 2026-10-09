import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


class SelesDataAnalyzer():

    def __init__(self):
        print("\n== Load Dataset ==")
        csv = input("Enter the Path of the Dataset (CSV file) :> ")
        self.data = pd.read_csv(csv)
        print("Data Loaded Successfully!")

    def explore_data(self):
        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 Row")
            print("2. Display the last 5 Row")
            print("3. Display column name")
            print("4. Display data type")
            print("5. Display basic info")
            print("6. Exit")

            sub_choice = int(input("\nEnter your Choice :> "))

            if sub_choice == 1:
                print("\nFirst 5 Row :>\n")
                print(self.data.head())

            elif sub_choice == 2:
                print("\nLast 5 Row :>\n")
                print(self.data.tail())

            elif sub_choice == 3:
                print("\nAll Column Name :>\n")
                print(self.data.columns)

            elif sub_choice == 4:
                print("\nData Type of Columns :>\n")
                print(self.data.dtypes)

            elif sub_choice == 5:
                print("\nBasic Info of Data :>\n")
                self.data.info()

            elif sub_choice == 6:
                print("\nBack to Main Manu !")
                break
            else:
                print("Invalid Choice !")


    def clean_data(self):

        missing_value = self.data[self.data.isnull().any(axis=1)]
        print("\n== Handle Missing Data ==")
        print("1. Display Row with Missing Value")
        print("2. Fill Missing Value With Mean")
        print("3. Drop Row With Missing Value")
        print("4. Replace missing value with a specific Value")

        s_choice = int(input("\nEnter your Choice :> "))

        if s_choice == 1:

            if len(missing_value) == 0:
                print("\nNo missing Value Found in Dataset !")

            else:
                print("\nRow with Missing Value :>\n")
                print(missing_value)

        elif s_choice == 2:
            if len(missing_value) == 0:
                print("\nNo missing Value Found in Dataset !")

            else:
                numeric_columns = self.data.select_dtypes( include="number" ).columns
                for i in numeric_columns:
                    self.data[i] = self.data[f"{i}"].fillna(self.data[f"{i}"].mean())
                print("\nMean Value Successfully Filled ")

        elif s_choice == 3:
            if len(missing_value) == 0:
                print("\nNo missing Value Found in Dataset !")

            else:
                self.data.dropna()
                print("\nRow Droped Succesfully !")

        elif s_choice == 4:
            if len(missing_value) == 0:
                print("\nNo missing Value Found in Dataset !")

            else:
                spe_value = int(input("Enter the Specific Value :> "))
                print(self.data.fillna(spe_value,inplace=True))


    def df_operation(self):
        print("\nPlease select an opetion :")
        print("1. Sort By Value")
        print("2. Filter With Value")

        s_choice = int(input("\nEnter your Choice :> "))

        if s_choice == 1:
            print("\n1. In Total sales")
            print("\n2. In Deals Closed")
            sub_ch = int(input("\nEnter the Choice :> "))

            if sub_ch == 1:
                sort = self.data.sort_values(by="Total Sales (INR)")
                print(sort)

            elif sub_ch == 2:
                sort = self.data.sort_values(by="Deals Closed")
                print(sort)

            else:
                print("\nInvalid Choice !")

        elif s_choice == 2:
            print("\n1. In Total sales")
            print("\n2. In Deals Closed")
            sub_ch = int(input("\nEnter the Choice :> "))

            if sub_ch == 1:
                value = int(input("\nEnter The Value to Filter :> "))
                df_filter = self.data[self.data["Total Sales (INR)" > {value}]]
                print(df_filter)

            elif sub_ch == 2:
                value = int(input("\nEnter The Value to Filter :> "))
                df_filter = self.data[self.data["Deals Closed" > {value}]]
                print(df_filter)

            else:
                print("\nInvalid Choice !")

    def statistics(self):
        print("\n == Descriptive Statistics == \n")
        print(self.data.describe())

    def data_vis(self):
        print("\n == Data Visualization ==")
        print("1. Bar Ploat")
        print("2. Line Ploat")
        print("3. Scatter Ploat")
        print("4. Histogram")
        print("5. Stack Ploat")

        sub_choice = int(input("\nEnter your Choice :> "))

        if sub_choice == 1:
            print("\n== Bar Ploat == ")
            x =input("\nEnter X axis Name :> ")
            y =input("Enter Y axis Name :> ")

            print("\nGenerating Bar Ploat")
            sb.barplot(data=self.data,x=f"{x}",y=f"{y}")
            plt.show()
            print("Bar Ploat Display Successfully !")

        elif sub_choice == 2:
            print("\n== Line Ploat == ")
            x =input("\nEnter X axis Name :> ")
            y =input("Enter Y axis Name :> ")

            print("\nGenerating Line Ploat")
            sb.lineplot(data=self.data,x=f"{x}",y=f"{y}")
            plt.show()
            print("Line Ploat Display Successfully !")

        elif sub_choice == 3:
            print("\n== Scatter Ploat == ")
            x =input("\nEnter X axis Name :> ")
            y =input("Enter Y axis Name :> ")

            print("\nGenerating Scatter Ploat")
            sb.scatterplot(data=self.data,x=f"{x}",y=f"{y}")
            plt.show()
            print("Scatter Ploat Display Successfully !")
            
        elif sub_choice == 4:
            print("\n== Histogram ==")
            x =input("\nEnter X axis Name :> ")
            print("\nGenerating Histogram")
            sb.histplot(data=self.data,x=f"{x}")
            plt.show()

            print("Histogram Display Successfully !")


while True:
    print("\n\t============= Data Analysis & Visualization Program =============")


    print("\nPlease select an opition :")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operation")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("=================================================================")



    choice = int(input("\nEnter your Choice :> "))

    if choice == 1:
        obj = SelesDataAnalyzer()

    elif choice == 2:
        obj.explore_data()

    elif choice == 3:
        obj.df_operation()

    elif choice == 4:
        obj.clean_data()

    elif choice == 5:
        obj.statistics()

    elif choice == 6:
        obj.data_vis()