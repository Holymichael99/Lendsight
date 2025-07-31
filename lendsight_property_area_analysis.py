import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------- Load and Prepare Data -------------------
df = pd.read_csv('loan.csv')

# Fill necessary missing values
df['Property_Area'] = df['Property_Area'].fillna('Unknown')
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
df['ApplicantIncome'] = df['ApplicantIncome'].fillna(0)
df['CoapplicantIncome'] = df['CoapplicantIncome'].fillna(0)

# Calculate Total Income
df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']

# ------------------- Plot 1: Loan Count by Property Area -------------------
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='Property_Area')
plt.title('Loan Count by Property Area')
plt.xlabel('Property Area')
plt.ylabel('Number of Loans')
plt.tight_layout()
plt.show()

# ------------------- Plot 2: Average Loan Amount by Property Area -------------------
plt.figure(figsize=(7, 5))
sns.barplot(data=df, x='Property_Area', y='LoanAmount')
plt.title('Average Loan Amount by Property Area')
plt.xlabel('Property Area')
plt.ylabel('Average Loan Amount')
plt.tight_layout()
plt.show()

# ------------------- Plot 3: Average Total Income by Property Area -------------------
plt.figure(figsize=(7, 5))
sns.barplot(data=df, x='Property_Area', y='TotalIncome')
plt.title('Average Total Income by Property Area')
plt.xlabel('Property Area')
plt.ylabel('Average Total Income')
plt.tight_layout()
plt.show()
