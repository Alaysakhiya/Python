arr=[]
total=0
largest=0
even=0
odd=0



print('''
      Select the choice :
 1. to creat the array
 2. to View the array
 3. to Sum of the array
 4. to Find largest number of the array
 5. to Find Smallest number of the array
 6. to Check Even or Odd number of the array
 7. to Revers the array
 8. to Check the Element is Exits
 9. to frequency of each element of array
 0. to Exit the programme
           ''')


while True:
    choice=int(input("\nEnter the choice => "))

    if choice==1:
        num=int(input("Enter the number to add element of the array : "))

        for i in range(num):
            ele=int(input(f"Enter the no.{i+1} element : "))
            arr.append(ele)

        print("\nArray is created !")

    elif choice==2:

        print(f"{arr}")

    elif choice==3:

        for i in arr:
            total +=i

        print(f"The sum of the array is => {total} ")

    elif choice==4:

        for i in arr:
            if i>=largest:
                largest=i

        print(f"The largest number of Array is => {largest}")  

    elif choice==5:

        smallest=arr[0]
        for i in arr:
            if i<=smallest:
                smallest=i

        print(f"The Smallest number of Array is => {smallest}")  

    elif choice==6:

        for i in arr:
            if i%2==0:
                even+=1
            else:
                odd+=1
        print(f"\nTotal Even number is => {even}")        
        print(f"Total Odd number is => {odd}") 


    elif choice==7:

        print("Revered Array is :",arr[::-1]) 


    elif choice==8:

        check=int(input("\nEnter the Element to check => "))

        if check in arr:
             print("Element is exits ")
        else:
             print("Element is not exits ")
                 

    elif choice==9:
        frequency={}
        for i in arr:
            if i in frequency:
                        frequency[i]+=1
            else:
                        frequency[i]=1

        for key,value in frequency.items():
                print(f"{key} ---={value} times in array")

    elif choice==0:
        print("\nProgramme is closed ! ")

        break


    else:
            print("\nInvalid !")
            break















