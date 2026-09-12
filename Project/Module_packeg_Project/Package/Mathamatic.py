import math

print("""
Mathematical Operation :
1. Calculate Factorial
2. Slove Compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Back to Main Manu

""")

while True:

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
                    pass
    elif choice == 4:
                    pass
    elif choice == 5:
                    pass

    else:
                    pass