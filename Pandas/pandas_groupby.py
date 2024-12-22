import pandas as pd

# Splitting the Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago'],
    'Sales': [100, 200, 300, 150, 250, 350]
}
df = pd.DataFrame(data)
grouped = df.groupby('City')
print(grouped)


# Applying Functions
# Calculate the sum of sales for each city
sum_sales = grouped['Sales'].sum()
print(sum_sales)

# Calculate the mean of sales for each city
mean_sales = grouped['Sales'].mean()
print(mean_sales)


# Iterating Over Groups
for name, group in grouped:
    print(name)
    print(group)


# Multiple Grouping Columns
grouped_multiple = df.groupby(['Name', 'City'])
print(grouped_multiple['Sales'].sum())


# Aggregating with Multiple Functions
grouped_agg = grouped['Sales'].agg(['sum', 'mean', 'count'])
print(grouped_agg)


# A complete example

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago'],
    'Sales': [100, 200, 300, 150, 250, 350]
}
df = pd.DataFrame(data)

# Group by a single column
grouped = df.groupby('City')

# Sum of sales for each city
sum_sales = grouped['Sales'].sum()
print("Sum of sales for each city:")
print(sum_sales)

# Mean of sales for each city
mean_sales = grouped['Sales'].mean()
print("\nMean of sales for each city:")
print(mean_sales)

# Iterating over groups
print("\nIterating over groups:")
for name, group in grouped:
    print(f'City: {name}')
    print(group)

# Group by multiple columns
grouped_multiple = df.groupby(['Name', 'City'])
print("\nSum of sales for each (Name, City) pair:")
print(grouped_multiple['Sales'].sum())

# Aggregating with multiple functions
grouped_agg = grouped['Sales'].agg(['sum', 'mean', 'count'])
print("\nAggregating with multiple functions:")
print(grouped_agg)
