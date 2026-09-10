from datetime import datetime


print("""
DateTime and Time Operation :
1. Display Current Date and Time
2. Calculate diffrence between Two Time
3. Format Date into Custome Format
4. StopWatch
5. Countdown Timer 
6. Back to Main Menu
""")

while True:

        sub_choice = int(input("Enter the Choice :> "))

        if sub_choice == 1:
            current_time = datetime.now()
            print(f"Current Date and Time :> {current_time}")
        elif sub_choice == 2:
            pass
        elif sub_choice == 3:
            pass
        elif sub_choice == 4:
            pass
        elif sub_choice == 5:
            pass
        elif sub_choice == 6:
            pass
        else:
            pass
