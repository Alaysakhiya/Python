


from datetime import datetime

current_time = datetime.today().date()

format_date = datetime.strftime(current_time, "%d/%m/%Y")

print(current_time)
print(format_date)
