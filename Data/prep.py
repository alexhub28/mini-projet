import pandas as pd
print("hello")


# load penguins_raw.csv
df = pd.read_csv("penguins_raw.csv")

print(df.head())
#rename columns
#Species,Island,Bill Length (mm),Bill Depth (mm),Flipper Length (mm),Body Mass (g),Sex,Date Collected,Observer,Notes
#to
#species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
df = df.rename(columns={
    "Species": "species",
    "Island": "island",
    "Bill Length (mm)": "bill_length_mm",
    "Bill Depth (mm)": "bill_depth_mm",
    "Flipper Length (mm)": "flipper_length_mm",
    "Body Mass (g)": "body_mass_g",
    "Sex": "sex",
    "Date Collected": "date",
    "Observer": "observer",
    "Notes": "notes"
})

print(df.head())

#drop columns Date, observer, notes
df = df.drop(columns=["date", "observer", "notes"])

print(df.head())

#if there is a missing value in the sex column, fill this value with UNKNOWN
df["sex"] = df["sex"].fillna("UNKNOWN")

print(df.head())

#remove all rows with missing values
print(df.head()) 

# in the species column
# replace Adélie with Adelie
# replace adelie with Adelie
df["species"] = df["species"].replace("Adélie", "Adelie")
df["species"] = df["species"].replace("adelie", "Adelie")

print(df.head())

#print the unique values of the column sex
print(df["sex"].unique())

#in the column sex
#replace male with MALE
#replace m with MALE
#replace M with MALE
#replace female with FEMALE
#replace f with FEMALE
#replace F with FEMALE
#replace unknown with UNKNOWN
df["sex"] = df["sex"].replace("male", "MALE")
df["sex"] = df["sex"].replace("m", "MALE")
df["sex"] = df["sex"].replace("M", "MALE")
df["sex"] = df["sex"].replace("female", "FEMALE")
df["sex"] = df["sex"].replace("f", "FEMALE")
df["sex"] = df["sex"].replace("F", "FEMALE")
df["sex"] = df["sex"].replace("unknown", "UNKNOWN")


print(df["sex"].unique())

#what is the range of the column body_mass_g
print(df["body_mass_g"].min())
print(df["body_mass_g"].max())

#remove all rows where body_mass_g is negative 
df = df[df["body_mass_g"] > 0]

print(df["body_mass_g"].min())
print(df["body_mass_g"].max())

#remove alls rows where body_mass_g is greater than 10000
df = df[df["body_mass_g"] <= 10000]
print(df["body_mass_g"].min())
print(df["body_mass_g"].max())

#save the cleaned data to a penguins_cleaned.csv file
df.to_csv("penguins_cleaned.csv", index=False)  