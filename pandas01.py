import pandas as pd

data = {
    'student': ["Anna", "Brandon", "Celia"],
    'grade': [90, 92, 95]
}

df = pd.DataFrame(data) #import data into dataframe

print(df)
print("Just the head", df.head())
print("Tail 2 rows", df.tail(2))
print("Info", df.info())
print("Describe", df.describe())

df = pd.read_csv("titanic.csv")
print("The titanic data", df.head())

df.to_json('titanic_json_data.json')

df_only_age = df['Age']
print("Only age column", df.Age)

df_multiple_columns = df[['Age', 'Fare', 'Survived']]
print("Multiple columns", df_multiple_columns)

df_over_50 = df[df['Age']> 50]
print("Over 50", df_over_50)

df_surv_over_50 = df[(df['Age']>50) & (df['Survived'] == 1)]

df_children_second_class = df[(df['Age'] < 10) & (df['Pclass'] == 2)]

print("Without missing data in rows", df.dropna())
print("Without missing data in columns", df.dropna(axis=1))
print("No cabin data", df.drop("Cabin", axis=1))

df['Country'] = "Unknown"
print("Adding Country Column", df)

df_renamed = df.rename(columns={
    'PassengerId': "Passenger_ID",
    "SibSp": "Siblings_Spouses_Aboard",
    "Parch":"Parents_Children_Aboard"
})

print("Renamed", df_renamed)

print("Missing Values", df.isnull().sum)

df_ffill = df.fillna(method="ffill")
print("After FFill", df_ffill)


df['Age'] = df['Age'].fillna(df['Age'].mean())
print("After age fill", df['Age'].astype(int))

df = pd.read_csv("titanic.csv")
# Group by Pclass
grouped = df.groupby(["Pclass"])
# View the new groupings
for name, group in grouped:
    print(name)
    print(group)
avg_fare_by_class = grouped['Fare'].mean()
print("Avg fare by group", avg_fare_by_class)

fare_data = grouped['Fare'].agg(
    avg_fare=('mean'),
    median_fare=('median'),
    total_passengers=('count')
)

survived_data = grouped['Survived'].agg(
    avg_survived=('mean'),
    median_survived=('median'),
    total_passengers=('count')
)

data1 = {
'student': ["John", "Josh", "Jason"],
'grade': [100, 90, 95]
}
data2 = {
'student': ["Sam", "Sean", "Sarah"],
'grade': [80, 90, 100]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# Combining and Merging DataFrames
combined_on_rows = pd.concat([df1, df2], axis=0)
print("Combined on rows", combined_on_rows)
combined_on_cols = pd.concat([df1, df2], axis=1)
print("Combined on columns", combined_on_cols)
# Merging
merged = pd.merge(df1, df2, on="grade")
merged = pd.merge(df1, df2, how="left", on="grade")