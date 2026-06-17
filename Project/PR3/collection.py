print("\nWelcome to the Student Data Organizer ! ")

student=[ ]
while True:

    print('''\nSelect the choice
     Enter 1 to Add student
     Enter 2 to View the student
     Enter 3 to Update Information of student
     Enter 4 to Delete student
     Enter 5 to Display Subject
     Enter 0 to Exit
               ''')
    
    choice=int(input("Enter the your choice : "))

    if choice==1:

        print("\nEnter the Student Details: ")
        
        st=    {"Student Id" : (len(student)+1),
             "Name" : input("Name : ") ,
             "Age" : int(input("Age : ")),
             "Grade" : input("Grade : "),
             "Date of Birth" : tuple(input("Date of Birth(DD-MM-YYYY) : ")),
             "Subject" : set(input("Subject seprated by comma(,) : ").split(","))}

                
        student.append(st)
        print("\nStudent is successfully added !")

    elif choice==2:

        for st in student:
            print(f"ID : {st["Student Id"]}| Name : {st["Name"]}| Age : {st["Age"]}| Grade : {st["Grade"]} | Date of Birth : {(" ").join(st["Date of Birth"]) }|Subject : {(" ").join(st["Subject"])}")

        