import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------- Load the Dataset -------------------
df = pd.read_csv('loan.csv')

# ------------------- Data Cleaning -------------------
df['Credit_History'] = df['Credit_History'].fillna(0)
df['ApplicantIncome'] = df['ApplicantIncome'].fillna(0)
df['CoapplicantIncome'] = df['CoapplicantIncome'].fillna(0)
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']

# ------------------- Simulate Loan_Status if Missing -------------------
if 'Loan_Status' not in df.columns:
    df['Loan_Status'] = df['Credit_History'].apply(lambda x: 'Y' if x == 1.0 else 'N')

# ------------------- Plot 1: Loan Approval by Credit History -------------------
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='Credit_History', hue='Loan_Status')
plt.title('Loan Approval by Credit History')
plt.xlabel('Credit History (1 = Good, 0 = Poor)')
plt.ylabel('Count')
plt.legend(title='Loan Approved')
plt.tight_layout()
plt.show()

# ------------------- Plot 2: Total Income by Loan Status -------------------
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x='Loan_Status', y='TotalIncome')
plt.title('Total Income by Loan Approval Status')
plt.xlabel('Loan Status')
plt.ylabel('Total Income')
plt.tight_layout()
plt.show()

# ------------------- Plot 3: Credit History vs Income (Colored by Approval) -------------------
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='TotalIncome', y='Credit_History', hue='Loan_Status')
plt.title('Income vs Credit History Colored by Approval')
plt.xlabel('Total Income')
plt.ylabel('Credit History')
plt.tight_layout()
plt.show()

# ------------------- Plot 4: Impact of Credit History on Loan Amount -------------------
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x='Credit_History', y='LoanAmount')
plt.title('Impact of Credit History on Loan Amount Granted')
plt.xlabel('Credit History (1 = Good, 0 = Poor)')
plt.ylabel('Loan Amount')
plt.tight_layout()
plt.show()
