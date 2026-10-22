### INTRO TO PANDAS
import pandas as pd
data = {
    "Name": ["RM","Jin","Suga","Jhope"],
    "Age":[31,34,33,31],
    "Salary":[100000,80000,90000,95000]
}

df1 = pd.DataFrame(data)

# print(df1)

### BASIC FUNCTIONS AND METHODS

# print(df1.info())
# print(df1.head(2))
# print(df1.tail(1))
# print(df1.shape)
# print(df1.columns)
# df1.rename(columns={
#     "Name":"Member's name"
# },inplace=True)
# df2 = df1.rename(columns={
#     "Name":"Member's name"
# })
# print(df2)
# print(df1.describe())




