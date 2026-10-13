## READING A CSV FILE
# import csv
# filename = "data.csv" #file name
# fields = [] #column names
# rows = [] #data rows
#
# with open(filename,'r') as file:
#     file_reader = csv.reader(file) #reader object
#     fields = next(file_reader) #read header
#     rows = list(file_reader)
#     print(f"Total no. of rows: {len(rows)}") #row count
#
# print(f"Field names are:{", ".join(fields)}")
# print('\nFirst 5 rows are: \n')
# for row in rows[:5]:
#     for col in row:
#         print(f"{col:>10}",end=" ")
#     print()

## WRITING A CSV FILE

# import csv
# data = [
#     ["Name","Age"],
#     ["Roy",25],
#     ["Alice",24],
#     ["Bob",26]
# ]
# with open("students.csv","w",newline="") as file:
#     writer = csv.writer(file)
#
#     # Write single row
#     # writer.writerow(["Name","Age"])
#     # writer.writerow(["Roy",25])
#     # writer.writerow(["Alice",24])
#
#     # Write multiple rows
#     writer.writerows

## DICTIONARY BASED CSV HANDLING
## READING
# import csv
#
# with open("data.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)
#         # ACCESS BY COLUMN NAME
#         #print(f"{row["Name"]} {row["Marks(%)"]}")

## WRITING DICTIONARIES

import csv
data = [{
    "Name":"Harry",
    "Age":23,
    "City": "London"
},
    {
"Name": "Ginny",
        "Age": 20,
        "City": "NYC"
    },{
        "Name": "Luna",
        "Age": 22,
        "City": "NJ"
    }]
with open("data2.csv","w",newline="") as file:
    fields = ["Name", "Age","City"]
    writer = csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    # writer.writerow({
    #     "Name": "Harry",
    #     "Age": 23,
    #     "City": "London"
    # })
    # writer.writerow({
    #     "Name": "Ginny",
    #     "Age": 20,
    #     "City": "NYC"
    # })
    # writer.writerow({
    #     "Name": "Luna",
    #     "Age": 22,
    #     "City": "NJ"
    # })
    writer.writerows(data)
