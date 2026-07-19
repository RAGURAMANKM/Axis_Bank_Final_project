import pandas as pd

df = pd.read_csv("transactions.csv")

print(df.info())

print("\n")

print(df.head())

print("\nMissing Values")

print(df.isnull().sum())

print("\nDuplicate Rows")

print(df.duplicated().sum())

print("\nTransaction Types")

print(df["type"].value_counts())

print("\nSample Descriptions")

print(df["description"].sample(10, random_state=1))