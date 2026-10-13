## JSON FILE HANDLING

## CREATING A JSON FILE

# import json
# student = {
#     "Name": "Suranjana Roy",
#     "Age" : 24,
#     "City": "Kolkata"
# }
# with open("students.json","w") as file:
#     json.dump(student,file, indent=4)
#

## READING JSON FILES
import json
with open("students.json","r") as file:
    data = json.load(file)
print(data)