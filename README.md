# LendSight: Understanding the Patterns Behind Loan Applications

## 📌 Introduction
In today's evolving financial landscape, banks and lending institutions are inundated with loan applications daily. Understanding the patterns behind these applications—who applies, for how much, and under what conditions—is vital to making informed lending decisions and managing risk effectively.

**LendSight** is a data-driven project aimed at uncovering insights from a historical loan dataset. Through structured analysis and visualization, we explore demographic and financial factors that influence loan applications and approvals.

## 🎯 Objective
The primary objective of this project is to analyze loan application data to reveal trends, patterns, and segments that characterize different applicant types. This can aid in:
- Understanding who applies for loans and under what conditions.
- Identifying factors that influence loan approval decisions.
- Recognizing high-risk applicant profiles through clustering and credit behavior.

## 🧠 Data Source
- Source: [Kaggle](https://www.kaggle.com/datasets)
- Dataset Name: **Loan Prediction Dataset**
- Format: CSV

---

## 🔍 Analyses Performed

### 1. Exploratory Data Analysis (EDA)
We began by exploring the dataset to understand its structure, distributions, and completeness.

- **Distributions** of key numeric features such as `ApplicantIncome`, `LoanAmount`, and `Loan_Amount_Term`.
- **Count plots** for categorical variables like `Gender`, `Married`, and `Property_Area`.
- **Missing values** visualized using `missingno`, with a clear before-and-after comparison of imputation strategies.

 During EDA, we explored the loan dataset using visualizations to understand patterns, relationships, and red flags hidden in the data. Below are some key insights from the charts we generated:

 <img width="1196" height="872" alt="Screenshot 2025-07-31 135635" src="https://github.com/user-attachments/assets/3afe2403-ff9f-45eb-b4e3-c23043546255" />
 Applicant Income vs Coapplicant Income

This scatter plot compares how much the main applicant earns vs their co-applicant.

What we found: Most applicants either have no co-applicant or their co-applicant earns significantly less.

Why it matters: This helps banks see if both applicants can share the repayment burden or if one person is carrying all the risk.

<img width="1396" height="1024" alt="Screenshot 2025-07-31 135656" src="https://github.com/user-attachments/assets/6242f922-f3c4-46a0-8e9f-109dc07491f5" />
Total Income by Marital Status

This box plot compares total household income between married and unmarried applicants.

Insight: Married applicants generally have higher combined income, likely due to dual earners.

Impact: This could positively influence their loan approval chances since higher income means better repayment capacity.

<img width="1823" height="979" alt="Screenshot 2025-07-31 135715" src="https://github.com/user-attachments/assets/93afb00b-b93d-4587-8560-97696fc423b8" />

 Total Income by Education Level

This plot compares the total income of graduates vs non-graduates.

What we learned: Graduates tend to have a wider range of income, including some very high earners.

Takeaway: Education level could play a role in earning potential and financial stability.

<img width="1846" height="975" alt="Screenshot 2025-07-31 135735" src="https://github.com/user-attachments/assets/9531d2c4-ad49-4e5a-b1f9-fcfcb1728265" />
Loan Approval by Credit History

This chart shows how loan approvals are linked to credit history.

Finding: Applicants with a good credit history (1.0) were far more likely to be approved.

Conclusion: Credit score/history is a major factor in loan decisions, as it reflects repayment reliability.

<img width="990" height="664" alt="Screenshot 2025-07-31 135748" src="https://github.com/user-attachments/assets/281cda18-29c5-444a-9c6d-93ca4ef9b7a7" />
Loan Count by Property Area

This bar chart shows how many loan applications came from urban, semi-urban, and rural areas.

Observation: Semi-urban areas had the highest number of applicants.

Why it's useful: This helps institutions understand where most loan demand is coming from and possibly optimize outreach strategies.








 ##Loan Amount Analysis
In this section, we explored how loan amounts relate to various factors like income, gender, education, employment, and family size. The goal was to understand what influences the size of loans people apply for or receive.

- A **scatterplot** shows the relationship between `TotalIncome` and `LoanAmount`.

  <img width="788" height="529" alt="Screenshot 2025-07-31 141721" src="https://github.com/user-attachments/assets/aa2c0f5b-2327-4efc-ae07-402f078a470d" />
  Loan Amount vs. Total Income

This scatter plot shows the relationship between an applicant's total income and the loan amount they applied for. We noticed:

Most applicants with lower income tend to apply for smaller loans.

As income increases, the range of loan amounts also becomes wider, but very high loan amounts are less common.

A few outliers show some individuals with extremely high income and loan values.

What it means: Generally, people with higher income can afford (and are approved for) larger loans, but the trend isn't perfectly linear.

- **Bar plots** compare average loan amounts across `Gender`, `Education`, and `Self_Employed` categories.

  <img width="1793" height="566" alt="Screenshot 2025-07-31 141741" src="https://github.com/user-attachments/assets/f16f3786-557b-4014-9d74-c9043db3e968" />
   Loan Amount Analysis: Demographic Comparisons
The second image shows three side-by-side bar charts that compare the average loan amounts based on Gender, Education, and Self-Employment status. These comparisons help us understand how different personal or demographic factors may influence how much loan people apply for.

 1. Average Loan Amount by Gender
This chart compares the average loan amounts requested by males, females, and applicants with unknown gender.

Male applicants tend to request slightly higher loan amounts on average.

Female applicants request a bit less.

The "Unknown" category has the lowest average loan amount, though it could be due to missing data.

 Insight: There may be a slight tendency for male applicants to apply for more funding, but the differences aren’t extreme.

 2. Average Loan Amount by Education
Here, we compare loan amounts between graduates and non-graduates.

Graduates tend to apply for higher loan amounts.

Non-graduates apply for slightly lower amounts.

 Insight: Education level may be positively associated with higher loan requests, possibly due to better job prospects or confidence in repayment ability.

 3. Average Loan Amount by Self-Employment Status
This chart shows loan amounts based on whether someone is:

Self-employed

Not self-employed

Or has an unknown employment status

The results show:

Self-employed individuals request the highest loan amounts.

People who are not self-employed request less on average.

The "Unknown" category falls in the middle.

 Insight: Self-employed individuals might need more capital for business needs, which could explain their higher loan requests.

 Overall Takeaway:
This image makes it easy to compare how different groups behave when applying for loans. Gender, education, and employment type all seem to have moderate influence on the loan amount people request. These insights can help lenders better understand their applicants and tailor their loan products accordingly.

- Another plot highlights how loan amounts vary by the number of `Dependents`.
<img width="793" height="561" alt="Screenshot 2025-07-31 141750" src="https://github.com/user-attachments/assets/e1af76db-586f-49b8-825f-567ab96bc768" />


  Loan Amount Analysis: Impact of Number of Dependents
The third image is a bar chart that shows the average loan amount requested based on the number of dependents an applicant has. The categories are 0, 1, 2, and 3+ dependents.

 What the Chart Shows:
Applicants with 0 or 1 dependent request lower average loan amounts, around 130–135.

Those with 2 dependents request the highest average loan amount, going over 150.

Applicants with 3 or more dependents still request more than those with 0–1, but slightly less than those with 2 dependents.

 Insight:
As the number of dependents increases, applicants generally request higher loans, likely to meet greater financial responsibilities. However, beyond 2 dependents, the trend flattens a bit—possibly due to income limitations or more cautious borrowing behavior among larger families.

 Overall Takeaway:
This chart highlights a positive relationship between family size and the loan amount applied for. Financial institutions can use this insight to better assess loan eligibility and risk based on family responsibilities

## 3 Loan Income Analysis (Making Sense of Income Data)
To understand who’s applying for loans and whether they can afford to repay them, we looked at some key things: how much money people make, whether they have a coapplicant (like a spouse), and how factors like marital status and education play into income. Let’s break it down:

<img width="786" height="629" alt="Screenshot 2025-07-31 142725" src="https://github.com/user-attachments/assets/26e2d2fb-94da-41ca-8c92-a378585da569" />
 Applicant vs. Coapplicant Income

This chart shows us how much money both the main person applying (the applicant) and their coapplicant (if they have one) earn.

 What we noticed:

Most people who apply for loans make less than ₦10,000.

A lot of coapplicants don’t earn anything at all, meaning they probably don’t work or aren’t contributing financially.

Only a few people earn really high salaries (those are the dots far to the right or top).

 Why it matters:
This tells us that in most loan applications, it’s really the main applicant’s income that matters. So if that person doesn’t earn enough, the loan might not be approved—even if they have a coapplicant.

<img width="777" height="608" alt="Screenshot 2025-07-31 142736" src="https://github.com/user-attachments/assets/155929af-aa35-4042-b78c-d2de31f5e328" />
Total Income by Marital Status

Here, we compared total income (applicant + coapplicant) based on whether the person is married or not.

 What we found:

Married people tend to have slightly higher household incomes, possibly because there are two people contributing.

But it’s not a huge difference. Some single people also have high incomes.

Both married and single people can earn a lot—or very little.

 Why it matters:
Being married might help a little with household income, but it’s not a guarantee. Banks might see married applicants as slightly more financially stable, but both groups still vary a lot.

<img width="789" height="616" alt="Screenshot 2025-07-31 142746" src="https://github.com/user-attachments/assets/81979782-9d2e-4679-8277-b1f541ec1cf0" />
 Total Income by Education Level

Now we’re looking at income based on whether someone graduated from school (college or university) or not.

 Here’s what we saw:

People who are graduates usually make more money than those who didn’t graduate.

Graduates also had more cases of very high income, shown as dots above the boxes.

Non-graduates still earn money, but they’re more likely to earn less.

 Why it matters:
This shows that education plays a big role in how much people earn, which affects whether they’re likely to qualify for loans. More education can mean more income—and a better chance of getting approved.

 In short:

Most loan applicants don’t have very high incomes.

A lot of coapplicants don’t earn anything.

Being married or educated can slightly improve income, but it doesn’t guarantee financial strength.

This kind of income analysis helps banks and loan companies decide who’s likely to pay back their loans—and who might be at risk of defaulting.





### 4. Credit Worthiness Analysis
Understanding a person's creditworthiness is essential when evaluating their eligibility for a loan. In this section, we explore how credit history and income levels impact loan approvals and amounts using visual insights from our dataset.


  <img width="685" height="514" alt="Screenshot 2025-07-31 143341" src="https://github.com/user-attachments/assets/c66b4013-97f0-4b4b-b49d-55cd1a7b69e5" />
  
What it shows: This bar chart compares how many loans were approved or rejected based on an applicant’s credit history.

Interpretation:

Applicants with good credit history (1) are far more likely to get their loans approved.

Those with poor credit history (0) are mostly rejected.

What it means in simple terms: If you’ve been responsible with borrowing and repaying in the past, banks are more likely to say "yes" to your loan.

<img width="685" height="508" alt="Screenshot 2025-07-31 143352" src="https://github.com/user-attachments/assets/9935252a-eac9-4b1d-a21d-da6e59f9ef87" />

What it shows: This box plot compares the income levels of people who were approved vs rejected for loans.

Interpretation:

People with higher income are slightly more likely to get approved, but income alone isn’t the deciding factor.

We see both approvals and rejections across all income levels, including those with high income.

In simple terms: Earning more can help, but it’s not a guarantee — other things like credit history still matter.

<img width="785" height="623" alt="Screenshot 2025-07-31 143407" src="https://github.com/user-attachments/assets/c08b1361-ed35-4a94-be52-74485419eb61" />

What it shows: Each point represents a person, plotted by their income (x-axis) and credit history (y-axis). The color shows whether their loan was approved.

Interpretation:

Most of the blue dots (approved) are clustered at the top, where credit history = 1 (good).

The orange dots (rejected) are mainly at the bottom, where credit history = 0 (poor) — regardless of how much income they had.

In simple terms: Even if someone earns a lot, a bad credit history still leads to rejection. Good credit is key.

<img width="686" height="516" alt="Screenshot 2025-07-31 143420" src="https://github.com/user-attachments/assets/f7c112b6-d377-4101-9e07-84cb6893a451" />

What it shows: This chart looks at how the amount of money people are granted varies based on their credit history.

Interpretation:

The loan amounts are fairly similar, whether someone has a good or poor credit history.

But more extreme values (outliers) are seen among those with good credit — meaning they’re trusted with bigger loans sometimes.

In plain English: While average loan amounts don’t change much, people with good credit have a better shot at receiving large loans.

 What This Tells Us Overall
A good credit history is the single strongest signal banks look at when deciding to approve a loan.

Income plays a role, but not as strongly — someone with high income but bad credit may still get rejected.

To increase the chances of loan approval and access to bigger loan amounts, maintaining a strong credit history is crucial.







### 5. Property Area Analysis
This section explores how different property locations — Urban, Semiurban, and Rural — relate to key loan metrics in our dataset.

<img width="686" height="529" alt="Screenshot 2025-07-31 144138" src="https://github.com/user-attachments/assets/432636a3-a369-4ac9-8a15-34d894fdc2b0" />
Loan Count by Property Area

 What it shows:
This chart tells us how many loans were given out in each property area.

 Insight for Everyone:
Urban areas had the highest number of loans, followed by Semiurban and then Rural areas. This could mean more people in cities are applying for and receiving loans — possibly due to higher population or more financial institutions available.

<img width="681" height="517" alt="Screenshot 2025-07-31 144148" src="https://github.com/user-attachments/assets/6ac2f17f-b524-4b0b-ba15-bac6d645b66e" />
Average Loan Amount by Property Area

 What it shows:
This chart displays the average amount of money loaned to applicants in each area.

 Insight for Everyone:
Surprisingly, even though urban areas had more loan approvals, the average loan amounts are very similar across all areas. This suggests that loan size does not significantly depend on where someone lives, but possibly on other factors like income or employment.

<img width="684" height="520" alt="Screenshot 2025-07-31 144200" src="https://github.com/user-attachments/assets/a1b08348-6b14-4ea4-850f-c9afbb4ea1d3" />
Average Total Income by Property Area

 What it shows:
This chart compares the average total income (combined income of applicant and co-applicant) in each area.

 Insight for Everyone:
Rural applicants have slightly higher average total income than their urban and semiurban counterparts, although the difference isn't very large. This might indicate that income levels are not strictly tied to location — people in rural areas can earn just as much as those in cities.
 Summary Takeaway
While urban areas lead in the number of loan approvals, the amount borrowed and total income levels are quite balanced across all areas. This could mean that lenders treat applicants fairly regardless of location, and that income potential isn't limited to cities.



### 6.  Segmentation Analysis (Clustering of Loan Applicants)
To better understand our applicants and identify different types of customers, we used clustering (a machine learning technique) to group similar applicants based on their income and the loan amount they requested. This helps lenders tailor strategies based on customer profiles and risk.

<img width="782" height="626" alt="Screenshot 2025-07-31 144738" src="https://github.com/user-attachments/assets/659bf640-bf5e-4d70-af3e-0676d0a3dcc1" />
Scatter Plot: Applicant Segmentation (Income vs Loan Amount)
This scatter plot shows three clusters of applicants based on their income and the loan amount they applied for:

Red dots (Cluster 0): These are applicants with low to moderate income and smaller loan amounts. This group forms the majority.

Blue dots (Cluster 1): These applicants have very high incomes and often request large loan amounts. They are fewer but financially stronger.

Green dots (Cluster 2): These are scattered in the low-to-mid income range, with varying loan amounts. This cluster is relatively small.

 Takeaway: This segmentation helps us understand how income levels and loan demands relate, and it highlights which customers belong to which financial behavior group.

 <img width="692" height="568" alt="Screenshot 2025-07-31 144749" src="https://github.com/user-attachments/assets/e507d668-778b-4833-a873-9ed1b27fe4fc" />
 Bar Chart: Cluster Composition by Risk Profile
This chart shows how many applicants in each cluster fall into low-risk or high-risk categories:

Cluster 0 has the largest number of applicants. It also contains a good mix of low- and high-risk profiles.

Cluster 1, despite representing high-income applicants, has relatively few people, most of whom are low-risk.

Cluster 2 has a smaller number of applicants, mostly low-risk as well.

 Takeaway: Most of our customers fall into Cluster 0. But it also contains a large portion of high-risk individuals, which needs attention.

 <img width="782" height="533" alt="Screenshot 2025-07-31 144759" src="https://github.com/user-attachments/assets/10cb6890-2f98-4f5d-84a9-8a3917ac4af0" />
 Stacked Bar Chart: Proportion of Risk Profiles Within Each Cluster
This plot shows the proportion (percentage) of high-risk vs. low-risk applicants in each cluster:

In Cluster 0, about 25% are high-risk and 75% are low-risk.

In Cluster 1, the high-risk portion is even smaller, meaning this group is generally safer.

Cluster 2 also shows a high percentage of low-risk applicants.

 Takeaway: While Cluster 1 appears safest, Cluster 0 is the largest group but carries the most high-risk individuals. This helps lenders know where to focus attention in terms of risk mitigation.

 Summary
By segmenting applicants into clusters, we can:

Understand customer behavior based on income and loan needs

Identify which groups are safer or riskier

Tailor credit and marketing strategies to suit each segment

This analysis adds intelligence to decision-making and supports more effective lending strategies.

### Project Summary: Understanding What Sells — Customer Choices & Pricing Impact in Food Retail
This project aims to understand customer purchasing behavior and how various factors—such as pricing, product category, and seasonality—influence sales in the food retail sector. Using data-driven techniques, we explore what products perform best, when customers buy more, and how price affects demand.

 Key Objectives
Identify top- and bottom-performing products by sales and revenue.

Uncover time-based patterns and trends in purchasing behavior.

Analyze product categories to understand which drive the most volume and value.

Explore how sensitive customers are to price changes.

Segment customers based on income, loan amount (for credit data), and risk profiles to assist in strategic decision-making.

 Techniques Used
Exploratory Data Analysis (EDA): To uncover trends, outliers, and performance drivers.

Time Series Analysis: To detect seasonal trends and monthly/weekly patterns in sales.

Price Sensitivity Analysis: To study how product pricing impacts quantity sold across categories.

Clustering (Segmentation): To group similar customers by financial behavior and risk using unsupervised learning.

Visualization: For translating insights into clear, compelling visuals that support decision-making.

 Insights Gained
Some products consistently drive sales volume while others contribute more to revenue.

Sales show seasonal spikes during certain months and dips in others—useful for inventory and marketing planning.

Price and demand are often inversely related; customers are more sensitive to price in some categories than others.

Clustering analysis reveals distinct customer segments, allowing for personalized marketing and risk-aware lending strategies.

 Business Value
This project enables retail businesses and financial analysts to:

Make data-backed inventory and pricing decisions

Launch targeted promotions based on seasonality and category trends

Identify high-value customer groups and optimize for profitability

Understand which customer segments are higher risk or more price-sensitive




---

##  Technologies Used

- **Programming Language:** Python
- **Libraries:** 
  - Data Handling: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`, `missingno`
  - Machine Learning: `scikit-learn` (for KMeans clustering)
  - Scaling: `StandardScaler`
- **Data Cleaning and Imputation:** Mode, Median-based filling

---

##  Running the Code

1. Clone or download the project folder.
2. Make sure `loan.csv` is in the same directory as the notebook or script.
3. Install the required packages using pip if you haven't:

```bash
pip install pandas numpy matplotlib seaborn missingno scikit-learn
```

4. Run each section of the script as shown, or execute the notebook step-by-step to visualize outputs.
5. Results will appear as graphs and summary tables for each analytical objective.

---

##  Conclusion


  ## Project Status

 Complete — Models and insights validated. Ready for presentation, reporting, or deployment.
By analyzing applicant income, loan behavior, property preferences, and credit history, we gain meaningful insights into loan application trends. The project helps surface characteristics of high-risk and low-risk applicants, which is critical in shaping data-driven lending strategies.

## Author

**Damilare Igbosanya**

----------
## License

This project is released for educational and portfolio purposes.
