import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('loan.csv')

# Clean the data
df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
df['Gender'].fillna('Unknown', inplace=True)
df['Self_Employed'].fillna('Unknown', inplace=True)
df['Dependents'] = df['Dependents'].replace('3+', 3).fillna('0')
df['Dependents'] = df['Dependents'].astype(str)