import pandas as pd

dir1 = 'C:/Users/e11135/Downloads/bally_database2524-2025.csv'
dir2 = 'C:/Users/e11135/Downloads/bally_database2524-2024.csv'

df2025 = pd.read_csv(dir1,index_col=0)
df2024 = pd.read_csv(dir2,index_col=0)

index = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#%%

df_2024sales = df2024.iloc[:,1:5]

#df_2024sales['TTL_Sales'] = df_2024sales.sum(axis=1)

#%%

df_2024AOV = df2024.iloc[:,5:10]

df_2024Order = df2024.iloc[:,-5:]
#%%
'''df_2024sales.loc['TTL'] = df_2024sales.sum()
df_2024AOV.loc['TTL'] = df_2024Order.sum()
df_2024Order.loc['TTL'] = df_2024Order.sum()'''

#%%
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid')

fig, ax1 = plt.subplots(figsize=(16,10))

sns.barplot(x=df_2024sales.index,y=df_2024sales.TTL_Sales,color='y',ax =ax1,label='Sales')
sns.lineplot(x=df_2024sales.index,y=df_2024AOV['TTL_AOV.'],color='g',label='AOV.',marker='*',sizes=(20, 200),legend=False)

for i, v in enumerate(df_2024sales.TTL_Sales):
    ax1.text(i, v + 0.5, str(v), ha='center', va='bottom',rotation=45)

ax2 = ax1.twinx()
ax2.grid(True, which='major', linestyle='--', color='gray')
#sns.lineplot(x=df_2024sales.index,y=df_2024AOV['TTL_AOV.'],color='g',label='AOV.',marker='*',sizes=(20, 200),legend=False)
sns.lineplot(x=df_2024sales.index, y= df_2024Order['TTL_Orders'],color = 'r',ax =ax2,label='Orders',marker='o')

plt.legend()
plt.show()

#%%


'''
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]       # 左側 Y 軸
y2 = [100, 200, 300, 400, 500]  # 右側 Y 軸

fig, ax1 = plt.subplots()

# 左側 Y 軸線
ax1.plot(x, y1, color='blue', label='Y1 資料')
ax1.set_ylabel('Y1 軸', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# 建立右側 Y 軸
ax2 = ax1.twinx()
ax2.plot(x, y2, color='red', label='Y2 資料')
ax2.set_ylabel('Y2 軸', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title("雙 Y 軸範例")
plt.show()'''