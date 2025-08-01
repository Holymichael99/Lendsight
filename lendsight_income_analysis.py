import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('loan.csv')

# Clean and prepare data
df['Married'] = df['Married'].fillna('Unknown')
df['Education'] = df['Education'].fillna('Unknown')
df['ApplicantIncome'] = df['ApplicantIncome'].fillna(0)
df['CoapplicantIncome'] = df['CoapplicantIncome'].fillna(0)
df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']

# --- Plot 1: Applicant vs. Coapplicant Income Patterns ---
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='ApplicantIncome', y='CoapplicantIncome')
plt.title('Applicant vs. Coapplicant Income')
plt.xlabel('Applicant Income')
plt.ylabel('Coapplicant Income')
plt.tight_layout()
plt.show()

# --- Plot 2: Total Income by Marital Status ---
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Married', y='TotalIncome')
plt.title('Total Income by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Total Income')
plt.tight_layout()
plt.show()

# --- Plot 3: Total Income by Education Level ---
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Education', y='TotalIncome')
plt.title('Total Income by Education Level')
plt.xlabel('Education')
plt.ylabel('Total Income')
plt.tight_layout()
plt.show()

