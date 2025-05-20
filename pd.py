import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns



sheet_id = "159DhATOdzPM_FchBUWd-0qL8GEbm3TLeVLTE3KMNKVI"
sheet_name = "2025_"
index = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

#url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
bally_2025_url = "https://docs.google.com/spreadsheets/d/159DhATOdzPM_FchBUWd-0qL8GEbm3TLeVLTE3KMNKVI/edit?gid=1861784587"
bally_2024_url = "https://docs.google.com/spreadsheets/d/159DhATOdzPM_FchBUWd-0qL8GEbm3TLeVLTE3KMNKVI/gviz/tq?tqx=out:csv&sheet=2024_"

dir1 = 'C:/Users/e11135/Downloads/bally_database2524-2025.csv'
dir2 = 'C:/Users/e11135/Downloads/bally_database2524-2024.csv'

df2025 = pd.read_csv(dir1,index_col=0)
df2024 = pd.read_csv(dir2,index_col=0)

df_2024sales = df2024.iloc[:,1:5]
df_2024AOV = df2024.iloc[:,5:10]
df_2024Order = df2024.iloc[:,-5:]

df_2025sales = df2025.iloc[:,1:5]
df_2025AOV = df2025.iloc[:,5:10]
df_2025Order = df2025.iloc[:,-5:]

sns.set_theme(style='whitegrid')

fig, ax1 = plt.subplots(figsize=(8,5))

sns.barplot(x=df_2024sales.index,y=df_2024sales.TTL_Sales,color='y',ax =ax1,label='Sales')
sns.lineplot(x=df_2024sales.index,y=df_2024AOV['TTL_AOV.'],color='g',label='AOV.',marker='*',sizes=(20, 200),legend=False)

for i, v in enumerate(df_2024sales.TTL_Sales):
    ax1.text(i, v + 0.5, str(v), ha='center', va='bottom',rotation=45)

ax2 = ax1.twinx()
ax2.grid(True, which='major', linestyle='--', color='gray')
#sns.lineplot(x=df_2024sales.index,y=df_2024AOV['TTL_AOV.'],color='g',label='AOV.',marker='*',sizes=(20, 200),legend=False)
sns.lineplot(x=df_2024sales.index, y= df_2024Order['TTL_Orders'],color = 'r',ax =ax2,label='Orders',marker='o')

plt.legend()
#plt.show()

fig2, ax3 = plt.subplots(figsize=(8,5))
sns.barplot(x=df_2025sales.index,y=df_2025sales.TTL_Sales,color='y',ax =ax3,label='Sales')
sns.lineplot(x=df_2025sales.index,y=df_2025AOV['TTL_AOV.'],color='g',label='AOV.',marker='*',sizes=(20, 200),legend=False)
for i, v in enumerate(df_2025sales.TTL_Sales):
    ax3.text(i, v + 0.5, str(v), ha='center', va='bottom',rotation=45)
ax4 = ax3.twinx()
ax4.grid(True, which='major', linestyle='--', color='gray')
#sns.lineplot(x=df_2024sales.index,y=df_2024AOV['TTL_AOV.'],color='g',label='AOV.',marker='*',sizes=(20, 200),legend=False)
sns.lineplot(x=df_2025sales.index, y= df_2025Order['TTL_Orders'],color = 'r',ax =ax4,label='Orders',marker='o')
plt.legend()

fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=df_2025sales.index,
    y=df_2025sales.TTL_Sales,
    name='銷售額',
    marker_color='steelblue',
    yaxis='y1'
))

# 長條圖：利潤
fig3.add_trace(go.Bar(
    x=df_2025sales.index,
    y=df_2025AOV['TTL_AOV.'],
    name='利潤',
    marker_color='lightgreen',
    yaxis='y2'
))

# 折線圖：成長率（右側 Y 軸）
fig3.add_trace(go.Scatter(
    x=df_2025sales.index,
    y=df_2025Order['TTL_Orders'],
    name='訂單數',
    yaxis='y2',
    mode='lines+markers',
    line=dict(color='orange', width=3)
))

fig3.update_layout(
    title='雙 Y 軸：銷售/利潤 vs 成長率',
    xaxis=dict(title='月份'),
    yaxis=dict(title='Sales', side='left'),
    yaxis2=dict(title='Orders vs AOv.', overlaying='y', side='right'),
    legend=dict(x=0.01, y=0.99),
    barmode='group',
    template='plotly_white'
)



st.title("Read Google Sheet as DataFrame")

with st.container(border=True):
    st.subheader("這是一區塊")
    col1, col2 = st.columns([3, 3])

    with col1:
        st.header("2025 data")
        st.pyplot(fig2)

    with col2:
        st.header("2024 data")
        st.pyplot(fig)

    st.plotly_chart(fig3, use_container_width=True)