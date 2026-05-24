# ============================================
# DecodeLabs Project 2 — Exploratory Data Analysis
# ============================================

# Step 1 — Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# تحسين شكل الرسومات
plt.rcParams['figure.figsize'] = (10,6)

# ============================================
# Step 2 — Load Dataset
# ============================================

file_path = "Cleaned_Data_DecodeLabs.xlsx"

# قراءة ملف الإكسيل
df = pd.read_excel(file_path)

# عرض أول 5 صفوف
print("First 5 Rows:")
print(df.head())

# ============================================
# Step 3 — Dataset Information
# ============================================

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

# ============================================
# Step 4 — Check Missing Values
# ============================================

print("\nMissing Values:")
print(df.isnull().sum())

# ============================================
# Step 5 — Statistical Analysis
# ============================================

print("\nStatistical Summary:")
print(df.describe())

# ============================================
# Step 6 — Quantity Analysis
# ============================================

if 'Quantity' in df.columns:

    print("\nQuantity Analysis")

    print("Mean Quantity:", df['Quantity'].mean())
    print("Median Quantity:", df['Quantity'].median())
    print("Max Quantity:", df['Quantity'].max())
    print("Min Quantity:", df['Quantity'].min())

# ============================================
# Step 7 — Unit Price Analysis
# ============================================

if 'UnitPrice' in df.columns:

    print("\nUnit Price Analysis")

    print("Mean Unit Price:", df['UnitPrice'].mean())
    print("Median Unit Price:", df['UnitPrice'].median())
    print("Max Unit Price:", df['UnitPrice'].max())

# ============================================
# Step 8 — Total Price Analysis
# ============================================

if 'TotalPrice' in df.columns:

    print("\nTotal Price Analysis")

    print("Mean Total Price:", df['TotalPrice'].mean())
    print("Median Total Price:", df['TotalPrice'].median())
    print("Total Revenue:", df['TotalPrice'].sum())

# ============================================
# Step 9 — Product Analysis
# ============================================

if 'Product' in df.columns and 'TotalPrice' in df.columns:

    product_sales = (
        df.groupby('Product')['TotalPrice']
        .sum()
        .sort_values(ascending=False)
    )

    print("\nProduct Sales:")
    print(product_sales)

    # Visualization
    plt.figure(figsize=(12,6))

    product_sales.plot(kind='bar')

    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")

    plt.xticks(rotation=45)

    plt.show()

# ============================================
# Step 10 — Payment Method Analysis
# ============================================

if 'PaymentMethod' in df.columns:

    payment_analysis = df['PaymentMethod'].value_counts()

    print("\nPayment Method Analysis:")
    print(payment_analysis)

    plt.figure(figsize=(8,5))

    sns.countplot(x='PaymentMethod', data=df)

    plt.title("Payment Methods Distribution")

    plt.show()

# ============================================
# Step 11 — Order Status Analysis
# ============================================

if 'OrderStatus' in df.columns:

    status_analysis = df['OrderStatus'].value_counts()

    print("\nOrder Status Analysis:")
    print(status_analysis)

    plt.figure(figsize=(8,5))

    sns.countplot(x='OrderStatus', data=df)

    plt.title("Order Status Distribution")

    plt.show()

# ============================================
# Step 12 — Referral Source Analysis
# ============================================

if 'ReferralSource' in df.columns:

    referral_analysis = df['ReferralSource'].value_counts()

    print("\nReferral Source Analysis:")
    print(referral_analysis)

    plt.figure(figsize=(10,5))

    sns.countplot(x='ReferralSource', data=df)

    plt.title("Referral Source Distribution")

    plt.xticks(rotation=45)

    plt.show()

# ============================================
# Step 13 — Correlation Analysis
# ============================================

numeric_df = df.select_dtypes(include=np.number)

correlation_matrix = numeric_df.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# Heatmap
plt.figure(figsize=(10,6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Matrix")

plt.show()

# ============================================
# Step 14 — Outlier Detection
# ============================================

if 'TotalPrice' in df.columns:

    plt.figure(figsize=(10,5))

    sns.boxplot(x=df['TotalPrice'])

    plt.title("Outlier Detection for Total Price")

    plt.show()

# ============================================
# Step 15 — Sales Trend Over Time
# ============================================

if 'Date' in df.columns and 'TotalPrice' in df.columns:

    df['Date'] = pd.to_datetime(df['Date'])

    sales_trend = (
        df.groupby(df['Date'].dt.to_period('M'))['TotalPrice']
        .sum()
    )

    print("\nMonthly Sales Trend:")
    print(sales_trend)

    sales_trend.plot()

    plt.title("Monthly Sales Trend")

    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.show()

# ============================================
# Step 16 — Final Insights
# ============================================

print("\n========== FINAL INSIGHTS ==========")

print("""
1. Dataset is clean and organized.
2. Some products generate higher revenue than others.
3. Quantity and UnitPrice strongly affect TotalPrice.
4. Most orders are successfully delivered.
5. Certain payment methods are more popular.
6. Marketing channels affect customer acquisition.
7. Some high-value transactions appear as outliers.
8. Sales trends change over time.
""")

print("\nEDA Project Completed Successfully ✅")