### INTRO TO PANDAS
import pandas as pd
data = {
    "Name": ["RM","Jin","Suga","JHope"],
    "Age":[29,34,30,29],
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


### SAVE AND LOAD DATA FROM CSV

# df1.to_csv("Test_data.csv", index=False)
# load_df = pd.read_csv('Test_data.csv')
# print(type(load_df))
# print(load_df)

### ROWS & COLUMNS - SELECTION
# Columns Selection
#print(df1[["Name","Salary"]])
# Rows Selection
#print('\n\n')
## loc - label based index
#print(df1.loc[0])
#print()
#print(df1.loc[df1.Name=="RM"])
#print()
#print(df1.loc[(df1.Name == 'Suga') & (df1.Salary>=80000)])
#print('\n\n')
## iloc -> index-value based
#print(df1.iloc[2])
#print()
#print(df1.iloc[0:2]) #[start:stop:step]
#print('\n\n')


### FILTER DATAFRAME
print(df1['Age']>32) #boolean values
print()
print(df1[df1['Age']>32]) #printing true values only
# storing the filtered data in a new dataframe
print()
df_age_filter = df1[df1['Age']>32]
print(df_age_filter)
print()
#using multiple filters
print(df1[(df1['Age'] > 30) & (df1["Salary"]>70000)])
print()
## In the above method the dataframe size is getting changed for using filters
## but in the next method the size of the dataframe won't be changed
print(df1.where((df1['Age'] > 30) & (df1["Salary"]>70000)))
print()
print(df1.where(df1['Age'] > 30, other='Not Eligible'))
