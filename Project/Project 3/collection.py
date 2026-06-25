print("\nWelcome to the Student Data Organizer ! ")

student=[]
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
                "Subject" : set(input("Subject seprated by comma(,) : ").split(","))
                }

                
        student.append(st)
        print("\nStudent is successfully added !")

    elif choice==2:

        for st in student:
            print(f"ID : {st["Student Id"]} | Name : {st["Name"]} | Age : {st["Age"]} | Grade : {st["Grade"]} | Date of Birth : {(" ").join(st["Date of Birth"])} | Subject : {(" ").join(st["Subject"])}")

        
    elif choice==3:

        id=int(input("Enter ID to update the information of student : "))
        found=False

        for st in student:
                if id==st["Student Id"]:
                    found=True
                    st["Name"]= input("Name : ")
                    st["Age"] = int(input("Age : "))
                    st["Subject"]=set(input("Subject seprated by comma(,) : ").split(","))
                    st["Grade"] = input("Grade : ")

                    print("\nStudent is updated successfully !")

        if found==False:
            print("\nId is not found !")        

        
    elif choice==4:

        id=int(input("Enter ID to update the information of student : "))
        found=False

        for st in student:

            if id==st["Student Id"]:
                found=True
                student.remove(st)
                print("Student Deleted successfully !")

        if found==False:
            print("\nId is not found !") 


    elif choice==5:

        if len(student)==0:
            print("\nStudent not found")
        else:
            print("\nSubjects are : ")
            for st in student:
                print(f"Name : {st["Name"]} | Subject : {(" ").join(st["Subject"])}")

    elif choice==0:

        print("\nProgramme is Closed !")
        break

    else:
        print("\nInvalid !")

            

