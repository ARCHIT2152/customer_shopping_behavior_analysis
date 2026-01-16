# 🛒 Customer Shopping Behavior Analysis  
### End-to-End Data Analytics Project (Python | SQL | Dashboard)

## 📌 Project Overview
This project analyzes customer shopping behavior to uncover insights related to revenue, customer demographics, product categories, subscriptions, and discounts.  
It demonstrates a complete data analytics workflow using **Python, SQL, and dashboard visualization**, designed as a **portfolio project for Data Analyst internships**.

---

## 🎯 Objectives
- Identify top revenue-generating customer segments  
- Analyze category-wise and demographic-wise sales performance  
- Evaluate the impact of subscriptions and discounts on spending  
- Convert raw data into actionable business insights  

---

## 🧠 Dataset Summary
- **Customers:** ~3,900  
- **Average Purchase Amount:** $59.76  
- **Average Review Rating:** 3.75  
- **Subscription Rate:** 27%  
- Includes demographics, purchase behavior, discounts, subscriptions, and shipping details

---

## 🧹 Data Cleaning & Preparation (Python)
- Standardized column names to `snake_case`  
- Renamed `purchase_amount_(usd)` → `purchase_amount`  
- Handled missing values using median imputation  
- Converted purchase frequency to numeric values  
- Removed redundant columns  
- Loaded cleaned data into PostgreSQL using SQLAlchemy  

---

## 🛠 Tech Stack
- **Python:** Pandas, NumPy  
- **Database:** PostgreSQL  
- **Analysis:** SQL  
- **Visualization:** Power BI Dashboard  

---

## 🗄️ SQL Analysis
SQL queries were used to extract:
- Revenue by category, age group, and gender  
- Subscription vs non-subscription behavior  
- Discount impact on purchases  
- Customer segmentation (New, Returning, Loyal)  
- Top-performing products  

---

## 📊 Dashboard Insights
- Clothing is the top-performing category  
- Young Adults generate the highest revenue  
- Male customers generate higher revenue (157,890) than females (75,191)  
- Subscribed customers show higher average spending  
- Certain products are highly discount-dependent  

---

## 📈 Key Insights
- Clothing dominates both revenue and sales volume  
- Subscription adoption is low but linked to higher spend  
- Loyal customers contribute higher lifetime value  
- Discounts should be applied strategically  

---

## 💡 Business Recommendations
- Increase focus on high-performing categories like Clothing  
- Expand and promote subscription programs  
- Target Young Adults with personalized campaigns  
- Optimize discount strategies to avoid revenue loss  
- Improve engagement for underperforming segments  

---

## 🚀 What This Project Demonstrates
- Real-world data cleaning and preprocessing  
- Strong SQL-based analytical thinking  
- Business-focused insight generation  
- Dashboard-driven storytelling  
- End-to-end ownership of a data analytics project  

---

## ▶ How to Run
```bash
pip install pandas sqlalchemy psycopg2-binary
python analysis.py

