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

# Pandas - Analyzing DataFrames