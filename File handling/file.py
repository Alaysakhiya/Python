
# with open("File handling\\file1.txt", "r+") as a:

#     print(a.read())
#     a.write("Hi ALAY !!!\n")
#     a.write("Hi Everyone\n")
#     a.write("Everone is good \n")

#     print("==================")
#     a.seek(0)
#     print(a.read())

# c= b"DOGESH BHAI good sab thik hi\n"
# l= b"DOGESH BHAI good sab thik hi\n"
# d= b"DOGESH BHAI good sab thik hi\n"
# with open("File handling\\file1.txt","wb") as a:
#     a.write(c)
#     a.write(d)
#     a.write(l)

# with open("File handling\\file1.txt","rb") as a:
#     b= a.read()

# print(len(b.splitlines()))
# print(len(b))

with open("D:\\Python\\File handling\\full-moon-forest-night-dark-starry-sky-5k-8k-3840x2160-1684.jpg","rb") as a:
    b = a.read()

with open("D:\\Python\\File handling\\file.jpg","wb") as c:
    print(c.write(b))
