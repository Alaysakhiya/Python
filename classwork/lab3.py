
#              lab 3.2


# list=["appel","orenges","grapes","watermeloon","banana"]


# # print(list[1])
# # print(list[-1])

# list.append("mango")
# list.remove("appel")

# print(list)


# list.sort()
# print(list)

# list.reverse()

# print(list)

# list=["appel","orenges","grapes","watermeloon","banana"]

# li=[0,3]

# for i in li:
#     print(list)


# li=[32,92,61,16,32]


# for i in li:
#     if i==32:
#         li.remove(32)
        # print(li)


# print(li)


# t =(10,20,30)
# li=[10,20,30]


# # print(t)
# # print(t[0:4])
# # print(t[-1])
# # print(t[2])

# li[0]=60
# # t[0]=60

# print

                

# li=[0]
                
# for i in range(21):
        
#         li+=[i]
        
# print(li)


# even=[i for i in range(1,21)if i % 2==0]
# li2=even


# print (even)
# print(



# name="ALAy Sakhiya"

# vowel="aeiou"

# no=[char for char in name if char.lower() not in vowel]

# print("".join(no))

# t=(25,)
# print(t)
# del t


# set={62,152,32,62}

# print(set)

        
# set2= set ([1,9,6,6,5,2])
# # set3= set ([input("Enter the num = ")])
# print(set2)

# set={0,1,2,3,4,5}
# for i in set:
# #         print(i) 

# print(set)
# # remove=set.pop()


# print(set.pop())
# print(set)

# remove=set={0,1,2,3,4,5}

# remove.pop()
# print()

# set={1,2,4,5}
# set2={1,3,5,9,10}

# set2.add(6)
# set2.remove(3)

# print(2 in set2)
# print(set2)
# print(2 in set)
# print(set)


# set={1,2,3,4}
# set2={3,4,5,6}

# union=set2.union(set)
# print(union)
# print()

# inter=set.intersection(set2)
# print(inter)
# print()

# diff=set.difference(set2)
# set2.difference_update(set)
# print(diff)
# print(set2)

student=[

{"Id" : 1,"name": "Alay","age" : 18, "subject" : set(["eng,hindi"])},
{"Id" : 2,"name": "Avinash","age" : 23, "subject" : set(["eng,hindi"])},
{"Id" : 3,"name": "Krish","age" : 38, "subject" : set(["eng,hindi"])},
{"Id" : 4,"name": "Ayush","age" : 26, "subject" : set(["eng,hindi"])}
]




while True:
   
        print('''\nList of choice
              
        Enter 1 to add a student
        Enter 2 to view students
        Enter 3 to delete student
        Enter 4 to update student
        Enter 0 to exit              
                ''')

        choice=int(input("Enter the your choice : "))

        if choice==1:
                st ={
                        "Id" :len(student)+1,
                        "name": input("Enter the new student name : "),
                        "age" : int(input("Enter the new student age : ")),
                        "subject" : set(input("Enter the new student subjects by comma(,) : ").split(","))
                }

                student.append(st)

                print("\nStudent added successfully !" )

        elif choice==2:

                for i in student:
                        print(f"Id : {i["Id"]} Name : {i["name"]} subject : {", ".join((i["subject"]))}")


        elif choice==3:
                id=int(input("Enter the id to delete the student : "))
                found=False
                for i in student:
                        if i["Id"]-1==id-1:
                                student.remove(i)
                                found==True
                                print("\nStudent is deleted successfully !")
                                
                if found==False:
                        print("Student ID is not found")              

        elif choice==4:
                id=int(input("Enter the id to update the student : "))
                found=False
                for i in student:
                        if i["Id"]==id-1:
                                i["name"]=input("Enter the new student name : ")
                                i["subject"]= set(input("Enter the new student subjects by comma(,) : ").split(","))
                                i["age"]=int(input("Enter the new student age : "))

                if found==False:
                        print("Student ID is not found")  
        elif choice ==0:

                print("\nProgramme is successfully closed !")      
                break

        else:
                print("Invalid !")
                break

                                         

        








