import pandas as pd

# Identifying Missing Data
# Detecting Missing Data
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, 2, 3, None]
}
df = pd.DataFrame(data)
print(df.isna())


# Counting Missing Values
print(df.isna().sum())


# Handling Missing Data
# Dropping Missing Values
# Drop rows with any missing values
df_dropna_rows = df.dropna()

# Drop columns with any missing values
df_dropna_columns = df.dropna(axis=1)


# Filling Missing Values
# Fill missing values with a specific value
df_fillna_value = df.fillna(0)

# Forward fill (use the previous value to fill the missing value)
df_fillna_ffill = df.fillna(method='ffill')

# Fill with the mean of the column
df_fillna_mean = df.fillna(df.mean())

# If there are multiple columns then
df_fill = df['B'].fillna(value=df['B'].mean())


# Interpolating Missing Data
# Interpolation
df_interpolate = df.interpolate()


# A complete example

# Create a DataFrame with missing values
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, 2, 3, None]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Detecting missing values
print("\nMissing values (True indicates missing):")
print(df.isna())

# Counting missing values
print("\nCount of missing values in each column:")
print(df.isna().sum())

# Dropping rows with any missing values
df_dropna_rows = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropna_rows)

# Dropping columns with any missing values
df_dropna_columns = df.dropna(axis=1)
print("\nDataFrame after dropping columns with missing values:")
print(df_dropna_columns)

# Filling missing values with a specific value
df_fillna_value = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_fillna_value)

# Forward fill (use the previous value to fill the missing value)
df_fillna_ffill = df.fillna(method='ffill')
print("\nDataFrame after forward filling missing values:")
print(df_fillna_ffill)

# Fill with the mean of the column
df_fillna_mean = df.fillna(df.mean())
print("\nDataFrame after filling missing values with mean:")
print(df_fillna_mean)

# Interpolate missing values
df_interpolate = df.interpolate()
print("\nDataFrame after interpolating missing values:")
print(df_interpolate)
