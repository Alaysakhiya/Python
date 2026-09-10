
from datetime import datetime , time

current_time = datetime.today()


# print(current_time)
# print(format_date)

first_d = input("Enter the First Date (YYYY-MM-DD) : ")
second_d = input("Enter the Second Date (YYYY-MM-DD) : ")

date_1 = datetime.strptime(first_d,"%Y-%m-%d")
date_2= datetime.strptime(second_d,"%Y-%m-%d")

diffrence = (date_1 - date_2)

print(f"Difference :> {diffrence}")

