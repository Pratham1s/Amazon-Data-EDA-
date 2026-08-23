# 🛒 Amazon Product Data EDA

Exploratory data analysis on a raw Amazon product dataset (from Kaggle) — cleaning messy pricing/rating fields and answering business questions using Pandas, Matplotlib, and Seaborn.

## 📌 Overview

The raw dataset had prices stored as strings with ₹ symbols and commas, ratings with invalid placeholder values, and no consistent column naming. This project cleans the data end-to-end and answers a set of analytical questions about pricing, ratings, discounts, and product popularity across **1,465 products** spanning **211 categories**.

## 🛠️ Tech Stack
- 🐍 **Python** (Pandas) — data cleaning and aggregation
- 📊 **Matplotlib & Seaborn** — distribution and category visualizations

## 🧹 Data Cleaning
- Standardised column names (lowercase, stripped, spaces → underscores)
- Removed duplicate rows
- Converted `discounted_price` and `actual_price` from currency strings (e.g. `₹1,099`) to numeric floats
- Converted `discount_percentage` from string percentages (e.g. `64%`) to numeric floats
- Handled invalid rating entries (`|` placeholder values) by converting to null and imputing with the column mean
- Cleaned `rating_count` (removed commas) and imputed missing values with the column mean

## ❓ Questions Answered
1. What is the average rating for each product category?
2. What are the top-rated products (by rating count) within each category?
3. What is the distribution of discounted vs. actual prices?
4. How does average discount percentage vary across categories?
5. What are the most popular product names?
6. What are the most popular product keywords?
7. What is the correlation between discounted price and rating?
8. What are the top 5 categories with the highest average ratings?

## 📈 Key Findings
- 🏆 Top-rated category: **Computers & Accessories → Tablets** (4.6 average rating)
- 💸 Average discount across the catalog: **~47.7%**, ranging from 0% to 94%
- 🔁 Most frequently listed product: **Fire-Boltt Ninja Call Pro Plus Smart Watch** (5 listings)
- 📉 Discounted price vs. rating showed a **very weak positive correlation (0.12)** — price cuts don't meaningfully predict higher ratings in this dataset

## 📁 Files
| File | Description |
|---|---|
| `main.py` | Full cleaning + EDA pipeline |
| `amazon.csv` | Raw source dataset |

## 🔍 Data Source
Dataset sourced from Kaggle's public Amazon product dataset.
