# python-data-ml

- Python for Data Science and Machine Learning


## Python crash course

- Basic concepts of python language is needed.
- Data structures, arithmatic methods, conditional clauses, loops


## NumPy

- A Linear Algebra Library for Python. Important for data science with python.
- Almost all the libraries in PyData Ecosystem relies on NumPy.
- Has bindings to C libraries hence very fast.

```shell
conda install numpy
pip install numpy
```


### Numpy arrays

- Has two flavours;
    - Vectors - 1-d arrays
    - Matrices - 2-d arrays
- A Matrix can still have only one row or one column

### Arrays and Slices

- When a slice is created from an array, it refers to that part of the original array.
- Meaning that if the sliced array to be changed, then it'll affect the original array to be changed as well.


## Numpy Operations

- Array with Array operations
- Array with Scalar operations
- Universal Array Functions
- mat.sum(axis=i) where i is 0 <= i < dimension of the array


## Pandas

- It's an open source library built on top of NumPy.
- It allows for fast analysis and data cleaning and preparation.
- Excels in performance and productivity.
- Has built-in visualization features.
- Can work with data from a wide variety of sources.


### Series

- A `Series` is a one-dimensional labled array capable of holding any data type (integers, strings, floats, Python objects, etc.)
- Each elements in a `Series` is assigned a unique label known as the **index**. [pandas_series.py](./Pandas/pandas_series.py)
    - Creating a Series
    - Accessing Elements
    - Basic Operations
    - Common Methods
    - Indexing and Slicing


### DataFrames

- A `DataFrame` is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
- [pandas_dataframes.py](./Pandas/pandas_dataframes.py)
    - Creating a DataFrame
    - Accessing Data
    - Basic Operations
    - Common Methods
    - Indexing and Slicing

