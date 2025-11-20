import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


df = pd.read_csv("titanic.csv")
sns.set_theme()
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

surv_rate_sex = df.groupby("Sex")["Survived"].mean()
surv_rate_pclass = df.groupby("Pclass")["Survived"].mean()
surv_rate_embarked = df.groupby("Embarked")["Survived"].mean()
print(surv_rate_sex)
print(surv_rate_pclass)
print(surv_rate_embarked)

fig, axs = plt.subplots(1, 3, figsize=(18, 4))
sns.barplot(data=df, x="Sex", y="Survived", ax=axs[0])
sns.barplot(data=df, x="Pclass", y="Survived", ax=axs[1])
sns.barplot(data=df, x="Name", y="Survived", ax=axs[2])
plt.show()

columns_to_drop = ["PassengerId", "Name", "SibSp", "Parch", "Ticket",
"Fare", "Cabin"]
df_cleaned = df.drop(columns_to_drop, axis=1)
print(df_cleaned.columns)
print(df_cleaned.shape)

print(df_cleaned.isna().sum())

df_cleaned["Age"] = df["Age"].fillna(df["Age"].mean())
df_cleaned["Embarked"] = df["Embarked"].ffill()
print(df_cleaned.isna().sum())

features = ['Sex', 'Pclass', 'Age', 'Embarked']
target = "Survived"

X = df_cleaned[features]
y = df_cleaned[target]
X_encoded = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
X_encoded, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy: ", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))