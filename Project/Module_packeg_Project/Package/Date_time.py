from datetime import datetime
import time

class Datetime():
    def code():
        while True:
                print("""DateTime and Time Operation :
                1. Display Current Date and Time
                2. Calculate diffrence between Two Time
                3. Format Date into Custome Format
                4. StopWatch
                5. Countdown Timer 
                6. Back to Main Menu
                """)


                sub_choice = int(input("\nEnter the Choice :> "))

                if sub_choice == 1:
                    current_time = datetime.now()
                    print(f"Current Date and Time :> {current_time}")

                elif sub_choice == 2:

                    first_d = input("Enter the First Date (YYYY-MM-DD) : ")
                    second_d = input("Enter the Second Date (YYYY-MM-DD) : ")

                    date_1 = datetime.strptime(first_d,"%Y-%m-%d")
                    date_2= datetime.strptime(second_d,"%Y-%m-%d")

                    diffrence = (date_1 - date_2)

                    print(f"Difference :> {diffrence}")

                elif sub_choice == 3:
                    data = input("Enter the First Date (YYYY-MM-DD) : ")

                    new_data = datetime.strptime(data,"%Y-%m-%d")
                    format_date = datetime.strftime(new_data,"%d/%m/%Y")

                    print(f"New Formated Date :> {format_date}")

                elif sub_choice == 4:
                    second= int(input("Enter Second to Stop watch :> "))

                    for i in range (1,second +1):
                        time.sleep(1)
                        print(i)
                    print("Stop Watch is Over !")

                elif sub_choice == 5:
                    second= int(input("Enter Second to CountDown :> "))

                    print("CountDown is Start")
                    for i in range (second,0,-1):
                        time.sleep(1)
                        print(i)
                    print("CountDownn is Over !")

                elif sub_choice == 6:

                    print("Return To Main Manu !")
                    break

                else:
                    print("Invalid Choice !")
                    break
