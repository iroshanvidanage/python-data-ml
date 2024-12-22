import pandas as pd

# Creating a DataFrame
# From a dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)
print(df)

# From a list of lists
data_list = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 35, 'Los Angeles']
]
df_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print(df_list)


# Accessing Data
# Accessing columns
print(df['Name'])

# Accessing rows by index
print(df.iloc[0])  # First row

# Accessing rows by label
print(df.loc[0])  # First row if index starts from 0


# Basic Operations
df['Age'] = df['Age'] + 1  # Increment age by 1
print(df)


# Common Methods
print(df.head(2))  # First two rows
print(df.describe())  # Summary statistics
print(df.info())  # Information about the DataFrame


# Indexing and Slicing
print(df.iloc[1:3, 0:2])  # Rows 1 to 2 (inclusive), Columns 0 to 1 (exclusive)


# A complete example

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Accessing columns
print("\nAccess 'Name' column:")
print(df['Name'])

# Accessing rows by index
print("\nAccess first row using iloc:")
print(df.iloc[0])

# Basic operations
df['Age'] = df['Age'] + 1
print("\nDataFrame after incrementing age by 1:")
print(df)

# Statistical summary
print("\nSummary statistics:")
print(df.describe())

# Indexing and slicing
print("\nSlice DataFrame (rows 1 to 2, columns 0 to 1):")
print(df.iloc[1:3, 0:2])
