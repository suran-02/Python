import pandas as pd

df = pd.DataFrame([11,22,33], columns=['num_1'])
data = {
    "Name": ["RM","Jin","Suga","Jhope"],
    "Age":[31,34,33,31],
    "Role":["Leader","Vocalist","Rapper","Dancer"]
}

df1 = pd.DataFrame(data)

print(df1)