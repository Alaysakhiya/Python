
li=[]

print("Welcome to our programme")

while True:

    print('''\nSelect the choice
    Enter 1 create the array
    Enter 2 to read the array
    Enter 3 to delete the element of the array
    Enter 4 to update the element of the array
    Enter 0 to exit      
    ''')    

    choice=int(input("Enter the your choice : "))

    if choice==1:

        num=int(input("Enter hoe many elements to add to the array : "))

        for i in range(num):
            a=int(input(f"Enter the element value {i+1} => "))

            li.append(a)

        print("\n\nArrary is created !")

    elif choice==2:
        print()
        for i in li:
            print(i,end=" ")
        print()

    elif choice==3:
        idx= int(input("Enter the index number to remove : "))

        if idx>=0 and idx<len(li):
            li.pop(idx-1)
            print("\n Element Removed !")
        else:
            print("\nInvalid index !")
        idx= int(input("Enter the index number to remove : "))

    elif choice==4:
         idx= int(input("Enter the index number to update : "))
         val=int(input("Enter the new value : "))

         if idx>=0 and idx<len(li):
            li[idx-1]=val
            print("\n Element updatedd !")
         else:
            print("\nInvalid index !")
            
    elif choice==0:

        print("\n Thank You !\n")
        break


    else:
        print("\nInvalid choice !\n")

