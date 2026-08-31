import os

with open("hello.txt" , "w+") as a :

    # print(a.read())
    a.write("hello")
    a.seek(0)
    print(a.read())
os.remove("hello.txt")