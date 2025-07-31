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

# Create TotalIncome column
df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']

# --- Plot 1: Loan Amount vs Total Income ---
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='TotalIncome', y='LoanAmount')
plt.title('Loan Amount vs Total Income')
plt.xlabel('Total Income')
plt.ylabel('Loan Amount')
plt.tight_layout()
plt.show()