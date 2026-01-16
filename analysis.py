import pandas as pd

df = pd.read_csv("customer_shopping_behavior.csv")

#print(df.head)
#print(df.info())
#print(df.isnull().sum)
#print(df.isnull().values.any())

#print(df.isnull().sum())

df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(lambda x: x.fillna(x.median()))
#print(df.isnull().sum().sum())
#print(df.columns)
df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_"))
#print(df.columns)
df = df.rename(columns={'purchase_amount_(usd)' : 'purchase_amount'})


#creating age groups for better understanding of data
labels = ["young" ,"adults" ,"middle age" ,"older age"]
df["age_group"] = pd.qcut(df["age"],q=4,labels=labels)
#print(df[["age","age_group"]].head(10))

#changing frequency_of_purchases texts to numerical data
freq_mapping = {
    "Weekly": 7,
    "Fortnightly" : 14,
    "Quarterly" : 90,
    "Bi-Weekly" : 14,
    "Every 3 Months" : 90,
    "Monthly" : 30,
    "Annually" : 365
    }

df["freq_map"] =df['frequency_of_purchases'].map(freq_mapping)
#print(df["freq_map"].head())

#checking if both discount and promocode used values are same
#print((df["promo_code_used"] == df["discount_applied"]).all())

df = df.drop("promo_code_used",axis =1)

from sqlalchemy import create_engine

"""Step 1: Connect to PostgreSQL
Replace placeholders with your actual details"""

username = "postgres" # default user
password = "7898" # the password you set during installation
host = "localhost" # if running locally
port = "5432" # default PostgreSQL port
database = "customer_behavior" # the database you created in pgAdmin

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

#Step 2: Load DataFrame into PostgreSQL

table_name = "customer" # choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")
print(df.columns)
