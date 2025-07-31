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

# --- Plot 2: Average Loan Amount by Gender, Education, and Self-Employed ---
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.barplot(data=df, x='Gender', y='LoanAmount', ax=axes[0])
axes[0].set_title('Average Loan Amount by Gender')

sns.barplot(data=df, x='Education', y='LoanAmount', ax=axes[1])
axes[1].set_title('Average Loan Amount by Education')

sns.barplot(data=df, x='Self_Employed', y='LoanAmount', ax=axes[2])
axes[2].set_title('Average Loan Amount by Self-Employed Status')

plt.tight_layout()
plt.show()