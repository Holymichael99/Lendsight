import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

# Load Dataset
df = pd.read_csv("loan.csv")  # Adjust path if needed

# -------------------------------
# 1. Summary Information
# -------------------------------
print("Dataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------------
# 2. Distribution of Numeric Features
# -------------------------------
numeric_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

plt.figure(figsize=(12, 8))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(2, 2, i)
    sns.histplot(df[col], kde=True, color='skyblue')
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Count Plots for Categorical Features
# -------------------------------
categorical_cols = ['Gender', 'Married', 'Dependents', 'Education',
                    'Self_Employed', 'Credit_History', 'Property_Area']

plt.figure(figsize=(14, 12))
for i, col in enumerate(categorical_cols, 1):
    plt.subplot(3, 3, i)
    sns.countplot(data=df, x=col, palette='Set2')
    plt.title(f'Count Plot of {col}')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Visualize Missing Values BEFORE Imputation
# -------------------------------
print("\nMissing values BEFORE imputation:")
msno.matrix(df)
plt.title("Missing Values Before Imputation")
plt.show()

# Save missing counts BEFORE imputation (IMPORTANT: BEFORE filling missing values)
missing_before = df.isnull().sum()

# -------------------------------
# 5. Imputation Strategy (Basic)
# -------------------------------
# Fill categorical columns with mode
for col in ['Gender', 'Dependents', 'Self_Employed']:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Fill numerical columns
df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)

print("\nMissing values after imputation:")
print(df.isnull().sum())

# -------------------------------
# 6. Visualize Missing Values AFTER Imputation
# -------------------------------
print("\nMissing values AFTER imputation:")
msno.matrix(df)
plt.title("Missing Values After Imputation")
plt.show()

# Save missing counts AFTER imputation
missing_after = df.isnull().sum()

# -------------------------------
# 7. Bar Plot Comparison
# -------------------------------
# Only show columns that had missing data before imputation
missing_df = pd.DataFrame({
    'Before Imputation': missing_before,
    'After Imputation': missing_after
})

missing_df = missing_df[missing_df['Before Imputation'] > 0]

missing_df.plot(kind='bar', figsize=(10,6))
plt.title('Missing Values Before and After Imputation')
plt.ylabel('Count of Missing Values')
plt.xticks(rotation=45)
plt.show()
