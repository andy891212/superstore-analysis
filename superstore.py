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
