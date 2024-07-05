import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV file
data = pd.read_csv('creditcard.csv')

print(data)


# basic commands

# get first five rows of the dataset
print(data.head())

# Get summary statistics of the dataset
print(data.describe())

# Get information about the dataset
print(data.info())

# Check for missing values (is any null values or not)
print(data.isnull().sum())
