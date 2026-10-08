import pandas as pd


class SelesDataAnalyzer():

    def __init__(self):
        print("\n== Load Dataset ==")
        csv = input("Enter the Path of the Dataset (CSV file) :> ")
        self.data = pd.read_csv(csv)
        print("Data Loaded Successfully!")

    def explore_data(self):
        print("\n== Explore Data ==")
        print("1. Display the first 5 Row")
        print("2. Display the last 5 Row")
        print("3. Display column name")
        print("4. Display data type")
        print("5. Display basic info")

        sub_choice = int(input("\nEnter your Choice :> "))

        if sub_choice == 1:
            print("\nFirst 5 Row :>")
            print(self.data.head())

        elif sub_choice == 2:
            print("\nLast 5 Row :>")
            print(self.data.tail())

        elif sub_choice == 3:
            print("\nAll Column Name :>")
            print(self.data.columns)

        elif sub_choice == 4:
            print("\nData Type of Columns :>")
            print(self.data.dtypes)

        elif sub_choice == 5:
            print("\nBasic Info of Data :>")
            print(self.data.info())


    def clean_data(self):

        missing_value = self.data[self.data.isnull().any(axis=1)]
        print("\n== Handle Missing Data ==")
        print("1. Display Row with Missing Value")
        print("2. Fill Missing Value With Mean")
        print("3. Drop Row With Missing Value")
        print("4. Replace missing value with a specific Value")

        s_choice = int(input("Enter your Choice :> "))

        if s_choice == 1:

            if len(missing_value) == 0:
                print("\nNo missing Value Found in Dataset !")

            else:
                print("\nRow with Missing Value :>")
                print(missing_value)

        elif s_choice == 2:
            if len(missing_value) == 0:
                print("\nNo missing Value Found in Dataset !")

            else:

                for i in missing_value:
                    self.data[f"{i}"].fillna(self.data[f"{i}"].mean(),inplace=True)
                print("\nMean Value Successfully Filled ")

        elif s_choice == 3:
            if len(missing_value) == 0:
                print("\nNo missing Value Found in Dataset !")

            else:
                print(self.data.dropna())
                print("\nRow Droped Succesfully !")

        elif s_choice == 4:
            if len(missing_value) == 0:
                print("\nNo missing Value Found in Dataset !")

            else:
                spe_value = input("Enter the Specific Value :> ")
                print(self.data.fillna(spe_value))


    





print("\t============= Data Analysis & Visualization Program =============")


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



choice = int(input("Enter your Choice :> "))
