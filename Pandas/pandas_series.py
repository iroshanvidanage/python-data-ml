import pandas as pd

# Creating a Series
# From a list
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

# From a dictionary
data_dict = {'a': 1, 'b': 2, 'c': 3}
series_dict = pd.Series(data_dict)
print(series_dict)


# Accessing Elements
print(series[0])    # Access by position
print(series_dict['a'])  # Access by label


# Basic Operations
# Arithmetic operation
series = series + 10
print(series)

# Alignment based on index
series_2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(series_dict + series_2)


# Common Methods
print(series.head(2))  # First two elements
print(series.mean())   # Mean of the series
print(series.std())    # Standard deviation


# Indexing and Slicing
print(series[1:4])  # Elements from index 1 to 3


# A complete example

# Create a Series from a list
data1 = [10, 20, 30, 40, 50]
series1 = pd.Series(data1, index=['a', 'b', 'c', 'd', 'e'])
print("Original Series:")
print(series1)

# Accessing elements
print("\nAccess element by index label 'c':", series1['c'])

# Perform arithmetic operations
print("\nSeries after adding 5 to each element:")
print(series1 + 5)

# Statistical operations
print("\nMean of the Series:", series1.mean())
print("Standard Deviation of the Series:", series1.std())

# Indexing and slicing
print("\nSlice Series from index 'b' to 'd':")
print(series1['b':'d'])
