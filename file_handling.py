# f = open("new doc.txt", "r")
# print("Filename:", f.name)
# print("Mode:", f.mode)
# print("Is Closed?", f.closed)
#
# f.close()
# print("Is Closed?", f.closed)

# f = open("new doc.txt", "r")
# content = f.read()
# print(content)
# f.close()


# with open("new doc.txt", "w") as file:
#     file.write("Hello Python!\n")
#     file.write("File Handling is easy with Python.")
#
# print("File written successfully!")

#Instead of manually opening and closing the file,
# you can use the "with" statement, which automatically handles closing.
# This reduces the risk of file corruption and resource leakage.

# with open("new doc.txt","r") as file:
#     content = file.read()
#     print(content)


#Handling Exceptions When Closing a File

try:
    with open("geek.txt","r") as f:
        c = f.read()
        print(c)
except FileNotFoundError as e:
    print("Error: ",e)