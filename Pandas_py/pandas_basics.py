# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.

# Why Use Pandas?
# Pandas allows us to analyze big data and make conclusions based on statistical theories.

# Pandas can clean messy data sets, and make them readable and relevant
# Installation of Pandas
# C:\Users\Your Name>pip install pandas

import pandas as pd

# The version string is stored under __version__ attribute.
print(pd.__version__)

# What is a Series?
# A Pandas Series is like a column in a table.

# It is a one-dimensional array holding data of any type.
a=[1,2,3]
my_var= pd.Series(a)


# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

# This label can be used to access a specified value.
print(my_var[0])

# Creating Labels 
var= pd.Series(a, index=["x", "y", "z"])
print(var["z"])

# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.
cal = {
    "day1" : 23,
    "day2" : 430,
    "day3" : 450
}
print(pd.Series(cal))       #Note: The keys of the dictionary become the labels.

# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
print(pd.Series(cal, index=["day1", "day2"]))

# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

# Series is like a column, a DataFrame is the whole table.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df= pd.DataFrame(data)
print(df)
print()

# A Pandas DataFrame is a 2 dimensional data structure, \
# like a 2 dimensional array, or a table with rows and columns.

# Pandas use the loc attribute to return one or more specified row(s)
print(df.loc[0])

# Note: This example returns a Pandas Series.
print(df.loc[[0,1]])
# Note: When using [], the result is a Pandas DataFrame.
print()

# Named Indexes
# With the index argument, you can name your own indexes.
df = pd.DataFrame(data, index=["day1","day2", "day3"])

# Use the named index in the loc attribute to return the specified row(s).
print(df.loc["day2"])


# Load Files Into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.
file = r'C:\Users\Lakshya\OneDrive\Desktop\NumPy_Tutorial\Pandas_py\data.csv'
df= pd.read_csv(file)

print()
# Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).

# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

# Tip: use to_string() to print the entire DataFrame.

# max_rows
# The number of rows returned is defined in Pandas option settings.

# You can check your system's maximum rows with the pd.options.display.max_rows statement.
print(pd.options.display.max_rows)
pd.options.display.max_rows = 99

# Read JSON
# Big data sets are often stored, or extracted as JSON.

# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

# JSON = Python Dictionary

# JSON objects have the same format as Python dictionaries.
#df= pd.read_json('data.json')

# Pandas - Analyzing DataFramesViewing the Data

# One of the most used method for getting a quick overview of the DataFrame, is the head() method.

# The head() method returns the headers and a specified number of rows, starting from the top.

print(df.head(10)) # if not specified, the method will return 5 rows

# The tail() method returns the headers and a specified number of rows, starting from the bottom.

print(df.tail())
# The DataFrames object has a method called info(), that gives you more information about the data set.

print(df.info())
# The info() method also tells us how many Non-Null values there are present in each column, \
# and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

# Data Cleaning
# Data cleaning means fixing bad data in your data set.

# Bad data could be:

# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

new_df = df.dropna()
print(new_df.to_string())

# Note: By default,\
#  the dropna() method returns a new DataFrame, and will not change the original.

df.dropna(inplace=True)
# If you want to change the original DataFrame, use the inplace = True argument:

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

df.fillna(130, inplace=True)

# Replace Only For Specified Columns
df.fillna({"Cal":130}, inplace=True)

# Replace Using Mean, Median, or Mode. A common way to replace empty cells,\ is to calculate the mean, median or mode value of the column.
x = df["cal"].mean()
y = df["cal"].median()
z= df["cal"]. mode() [0]
df.fillna({"cal": x}, inplace= True)

# Data of Wrong Format
# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

# Convert Into a Correct Format
df['Date']= pd.to_datetime(df['Date'], format='mixed')

# Removing Rows
# The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, \
# and we can remove the row by using the dropna() method.

df.dropna(subset=['Date'], inplace=True)

# Wrong Data
# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

# Replacing Values--In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
df.loc[7, "duration"] =45   # for small dataset

#for larger dataset 

for x in df.index:
    if df.loc[x, "Dueration"] > 120:
        df.loc[x, "Duration"] = 120

# Removing Rows
# Another way of handling wrong data is to remove the rows that contains wrong data.

# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)
        
        
# Discovering Duplicates
# The duplicated() method returns a Boolean values for each row:
df.duplicated()

df. drop_duplicates(inplace=True)


# Pandas - Data Correlations
# Finding Relationships
# A great aspect of the Pandas module is the corr() method.

# The corr() method calculates the relationship between each column in your data set.
df.corr()
# Note: The corr() method ignores "not numeric" columns.

# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
# the number varies from -1 to 1

# 1 means there is a 1 to 1 relationship ( a perfect correlation), for each time the value went up \
# for first column, the other one went wp as well 

# 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

# -0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

# 0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

# say you have to have at least 0.6 (or -0.6) to call it a good correlation.


# Pandas Plotting 
import matplotlib.pyplot as plt

df.plot()
#plt.show()

# Scatter Plot--A scatter plot needs an x- and a y-axis.
df.plot(kind="scatter", x= "duration", y = "calories")
#plt.show()


#  the correlation between "Duration" and "Calories" was 0.922721, and we concluded with the fact that higher duration means more calories burned.

df.plot(kind="scatter", x= "Duration ", y= "Maxpulse")

# where there is a bad relationship between the columns, like "Duration" and "Maxpulse", with the correlation 0.009403
df["Duration"].plot(kind="hist")
