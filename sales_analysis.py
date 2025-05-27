
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure plots are displayed cleanly
sns.set(style="whitegrid")

# ---------------------------
# 1. Sales Distribution by Category (Pie Chart)
# ---------------------------
category_sales = dataset.groupby('Category')['Sales'].sum()
plt.figure(figsize=(8, 8))
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Category')
plt.axis('equal')
plt.show()

# ---------------------------
# 2. Total Sales by Category (Bar Chart)
# ---------------------------
plt.figure(figsize=(8, 6))
category_sales = dataset.groupby('Category')['Sales'].sum().sort_values(ascending=False)
sns.barplot(x=category_sales.values, y=category_sales.index, palette="viridis")
plt.title('Total Sales by Category')
plt.xlabel('Sales')
plt.ylabel('Category')
plt.tight_layout()
plt.show()

# ---------------------------
# 3. Total Profit by Sub-Category (Bar Chart)
# ---------------------------
plt.figure(figsize=(10, 8))
subcat_profit = dataset.groupby('Sub-Category')['Profit'].sum().sort_values()
sns.barplot(x=subcat_profit.values, y=subcat_profit.index, palette="magma")
plt.title('Total Profit by Sub-Category')
plt.xlabel('Profit')
plt.ylabel('Sub-Category')
plt.tight_layout()
plt.show()

# ---------------------------
# 4. Sales vs Profit by Category (Scatter Plot)
# ---------------------------
plt.figure(figsize=(8, 6))
sns.scatterplot(data=dataset, x='Sales', y='Profit', hue='Category')
plt.title('Sales vs Profit by Category')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.tight_layout()
plt.show()

# ---------------------------
# 5. Monthly Sales Trend (Line Plot)
# ---------------------------
# Convert 'Order Date' to datetime
dataset['Order Date'] = pd.to_datetime(dataset['Order Date'], errors='coerce')
dataset['Month'] = dataset['Order Date'].dt.to_period('M')
monthly_sales = dataset.groupby('Month')['Sales'].sum().sort_index()

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------
# 6. Total Sales by Region (Bar Chart)
# ---------------------------
plt.figure(figsize=(8, 6))
region_sales = dataset.groupby('Region')['Sales'].sum().sort_values()
sns.barplot(x=region_sales.values, y=region_sales.index, palette="coolwarm")
plt.title('Total Sales by Region')
plt.xlabel('Sales')
plt.ylabel('Region')
plt.tight_layout()
plt.show()
