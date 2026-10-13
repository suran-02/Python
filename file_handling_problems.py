#1 Create a file named doc.txt and write "Hello Python":
# with open("doc.txt","w") as file:
#     file.write("Hello Python")
#
# print("New doc created and populated successfully!")

#2 Read and print the contents of doc.txt.
# with open("doc.txt","r") as f:
#     print(f.read())

#3 Append the line: Learning File Handling to doc.txt
# with open("doc.txt","a") as f:
#     f.write("\nLearning File Handling")


#4 Read the first line of a file using readline().
# with open("doc.txt","r") as f:
#     print(f.readline())

#5 Create a file called numbers.txt. Store:
# 10
# 20
# 30
# 40
# 50
# each on a new line.

# arr = [10,20,30,40,50]
# with open("numbers.txt","w") as file:
#     for i in arr:
#         file.write(f"{i}\n")

#6 Read numbers.txt and find the sum of all numbers.
# with open("numbers.txt","r") as file:
#     # total = 0
#     # for line in file:
#     #     total+=int(line)
#     # print(total)
#     num_str = file.readlines()
#     print(sum(int(i) for i in num_str))

#7 Count the number of lines in a file
# with open("doc.txt","r") as file:
    # for line in file:
    #     cnt+=1
    # cnt = sum(1 for line in file)
    # print(cnt)
    ## when there are blanks in lines
    # cnt = 0
    # for line in file:
    #     if line.strip():
    #         cnt+=1
    # print(cnt)

#8 Count Total Words
# with open("doc.txt","r") as file:
#     total = 0
#     for line in file:
#         total += len(line.split())
#     print(total)

#9 Ask the user for a name and append it to users.txt
# st = input("Enter your name: ")
# with open("users.txt","a") as file:
#      file.write(st + "\n")

#10 Handle the case where a file does not exist.

# try:
#     with open("abc.txt","r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found!")


#10 Find the longest word in a file
with open("doc.txt","r") as file:
    # word = ""
    # for line in file:
    #     #word = [len(i) for i in line.split()]
    #     for i in line.split():
    #         if len(i)>len(word):
    #             word = i
    #
    # print(word)
    words = file.read().split()
    print(max(words,key=len))

