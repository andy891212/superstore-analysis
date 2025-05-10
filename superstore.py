import pandas as pd

# 加上 encoding 設定，改用 cp1252（或 ISO-8859-1 也可）
df = pd.read_csv(r"D:\py-training\superstore_project\SampleSuperstore.csv", encoding='cp1252')

# 確認資料
print(df.head())

# 查看資料基本資訊
print(df.info())
# 檢查每一欄是否有缺失值
print(df.isnull().sum())

import matplotlib.pyplot as plt
import seaborn as sns

# 例如：產品類型的銷售額分佈
plt.figure(figsize=(10,6))
sns.barplot(x='Category', y='Sales', data=df)
plt.title('Sales by Product Category')
plt.xticks(rotation=45)
plt.show()

print(df.columns)
print(df[['Region', 'City', 'Sales', 'Profit']].head())


# 將 Sales 和 Profit 依照 Region 和 City 分組並加總
grouped = df.groupby(['Region', 'City'])[['Sales', 'Profit']].sum().reset_index()

# 依照 Sales 排序，取前 10 名城市
top_sales = grouped.sort_values(by='Sales', ascending=False).head(10)

# 依照 Profit 排序，取前 10 名城市
top_profit = grouped.sort_values(by='Profit', ascending=False).head(10)

print("Top 10 Cities by Sales:")
print(top_sales)

print("\nTop 10 Cities by Profit:")
print(top_profit)


import matplotlib.pyplot as plt

# 銷售額視覺化
plt.figure(figsize=(10, 6))
plt.barh(top_sales['City'], top_sales['Sales'], color='skyblue')
plt.xlabel('Sales')
plt.title('Top 10 Cities by Sales')
plt.gca().invert_yaxis()
plt.show()

# 利潤視覺化
plt.figure(figsize=(10, 6))
plt.barh(top_profit['City'], top_profit['Profit'], color='lightgreen')
plt.xlabel('Profit')
plt.title('Top 10 Cities by Profit')
plt.gca().invert_yaxis()
plt.show()

# 檢查缺失值
print(df.isnull().sum())

# 填補缺失值（假設填補為0）
df.fillna(0, inplace=True)

# 檢查資料型別
print(df.dtypes)

# 先轉換 'Order Date' 欄位為日期格式
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 計算每一天的銷售額總和
daily_sales = df.groupby('Order Date')['Sales'].sum()

# 找出銷售額最高的日期
max_sales_date = daily_sales.idxmax()
max_sales_value = daily_sales.max()

print(f"The highest sales date is: {max_sales_date} with sales value: {max_sales_value}")
#The highest sales date is: 2014-03-18 00:00:00 with sales value: 28106.716



import matplotlib.pyplot as plt
import seaborn as sns

# 設定圖片風格
sns.set(style="darkgrid")

# 可視化每天的銷售額
plt.figure(figsize=(10, 6))
daily_sales.plot(kind='line')
plt.title("Daily Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()



# 計算每個產品的銷售總額
product_sales = df.groupby('Product Name')['Sales'].sum()

# 找出銷售額最高的產品
top_selling_product = product_sales.idxmax()
top_selling_product_sales = product_sales.max()

print(f"The top selling product is: {top_selling_product} with sales value: {top_selling_product_sales}")
#The top selling product is: Canon imageCLASS 2200 Advanced Copier with sales value: 61599.824

# 取得前10名銷售額最高的產品
top_10_products = product_sales.sort_values(ascending=False).head(10)

# 可視化前10名最暢銷的產品
plt.figure(figsize=(12, 6))
top_10_products.plot(kind='bar')
plt.title("Top 10 Best Selling Products")
plt.xlabel("Product Name")
plt.ylabel("Sales")
plt.xticks(rotation=90)
plt.show()
