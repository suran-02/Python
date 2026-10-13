## PROBLEMS ON CSV FILE HANDLING

##1 Read students.csv and print every row

# import csv
# with open("students.csv","r") as file:
#     file_reader = csv.reader(file)
#     next(file_reader)
#     for row in file_reader:
#         print(row)


##2 Read students.csv and Print only student names.

# import csv
# with open("students.csv","r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(row[0])


##3 Read students.csv and Count Total Students
# import csv
# with open("students.csv","r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     # rows = list(reader)
#     # print(f"The total count of the students -> {len(rows)}")
#     count = 0
#     for row in reader:
#         count += 1
#
#     print(count)


##4 Read students.csv and Find the oldest student
# import csv
# with open("students.csv","r") as file:
#     reader = csv.reader(file)
#     fields = next(reader)
#     age_index = fields.index("Age")
#     name_index = fields.index("Name")
#     oldest_age = -1
#     oldest_name = ""
#     for row in reader:
#         age = int(row[age_index])
#         if age > oldest_age:
#             oldest_age = age
#             oldest_name = row[name_index]
#
#     print(oldest_name)


## 5 Calculate average age.
import csv
with open("students.csv","r") as file:
    file_reader = csv.reader(file)
    fields = next(file_reader)
    age_index = fields.index("Age")
    cnt = 0
    total_age = 0
    for row in file_reader:
        total_age += int(row[age_index])
        cnt += 1
    avg = total_age/cnt
    print(f"Average of the ages -> {avg}")