import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ------------------- Load and Clean Data -------------------
df = pd.read_csv('loan.csv')

# Fill missing values
df['ApplicantIncome'] = df['ApplicantIncome'].fillna(0)
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].median())
df['Credit_History'] = df['Credit_History'].fillna(0)  # Used for risk tagging

# ------------------- Feature Selection -------------------
features = df[['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']]

# ------------------- Feature Scaling -------------------
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# ------------------- K-Means Clustering -------------------
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# ------------------- Plot Clusters -------------------
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='ApplicantIncome', y='LoanAmount', hue='Cluster', palette='Set1')
plt.title('Applicant Segmentation: Income vs Loan Amount')
plt.xlabel('Applicant Income')
plt.ylabel('Loan Amount')
plt.legend(title='Cluster')
plt.tight_layout()
plt.show()

# ------------------- Risk Profiling -------------------
# Tag applicants as 'High Risk' if Credit_History is 0, else 'Low Risk'
df['Risk_Profile'] = df['Credit_History'].apply(lambda x: 'Low Risk' if x == 1.0 else 'High Risk')

# ------------------- Cluster Composition by Risk -------------------
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='Cluster', hue='Risk_Profile')
plt.title('Cluster Composition by Risk Profile')
plt.xlabel('Cluster Group')
plt.ylabel('Applicant Count')
plt.legend(title='Risk Profile')
plt.tight_layout()
plt.show()

# ------------------- Optional: Summary Table -------------------
summary = df.groupby('Cluster')[['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']].mean()
print("\nCluster Feature Means:\n", summary)

risk_summary = df.groupby('Cluster')['Risk_Profile'].value_counts(normalize=True).unstack().fillna(0)
print("\nRisk Distribution per Cluster (%):\n", (risk_summary * 100).round(1))

# ------------------- Plot: Risk Profile Distribution per Cluster -------------------
risk_summary.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='coolwarm')
plt.title('Risk Profile Distribution by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Proportion of Applicants')
plt.legend(title='Risk Profile', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
