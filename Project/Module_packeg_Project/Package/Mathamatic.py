import math

class math():
    def code():

        while True:
            print("""Mathematical Operation :
            1. Calculate Factorial
            2. Slove Compound Interest
            3. Trigonometric Calculations
            4. Area of Geometric Shapes
            5. Back to Main Manu
            """)


            choice = int(input("Enter your Choice :> "))    

            if choice == 1:
                num = int(input("Enter the Number to Calculate Factorial :> "))

                print(f"Factorial : {math.factorial(num)}")

            elif choice == 2:

                amount = int(input("Enter The Base Amount :> "))
                interest_rate = int(input("Enter The  Rate of Interest in (%) :> "))
                year = int(input("Enter the Duration (in Year) :> "))

                base_amount = amount

                for i in range(year):
                    interest = (amount * interest_rate)/100
                    amount+=interest

                print(f"Compound Interest :> {amount - base_amount}")
                print(f"Final Amount :> {amount}")
                
            elif choice == 3:
                    angel = int(input("Enter the Degree to Calculate Trigonometric :>  "))

                    data = math.radians(angel)

                    print(f"Sin{angel}° Value is {math.sin(data)}")
                    print(f"Cos{angel}° Value is {math.cos(data)}")
                    print(f"Tan{angel}° Value is {math.tan(data)}")

            elif choice == 4:
                        print("""
        1. To Find Area of Square
        2. To Find Area of Triangle""")
                        sub_choice = int(input("Enter your choice :> "))

                        if sub_choice == 1:
                                side = int(input("Enter Length of One Side (Cm) :> "))
                                area =math.pow(side,2)

                                print(f"Area of Square is {area}Cm²")

                        elif sub_choice == 2:

                                base = int(input("Enter Length of the Base :> "))
                                height = int(input("Enter Length of the Height :> "))

                                area = (base*height) / 2
                                print(f"Area of Triangle is {area}")

                        else:
                                print("Invalid !")
            elif choice == 5:
                            print("Return to the Main Manu ")
                            break

            else:
                        print("Invalid !")