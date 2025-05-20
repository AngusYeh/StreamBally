import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import numpy as np

st.title("Read Google Sheet as DataFrame")

#url = "https://docs.google.com/spreadsheets/d/1kT2Ly7_wYwCKTrElsCpneihHmhwGX-DpzhCPN9jpXSo/edit?usp=sharing"
bally_2025_url = "https://docs.google.com/spreadsheets/d/1N9FdHxi3FH2ljvwXBWfLjiWg8FiQA065PA6y_tnFesY/edit?gid=306112751"
bally_2024_url = "https://docs.google.com/spreadsheets/d/1N9FdHxi3FH2ljvwXBWfLjiWg8FiQA065PA6y_tnFesY/edit?gid=58608386"


conn = st.connection("gsheets", type=GSheetsConnection)
df2025 = conn.read(spreadsheet=bally_2025_url)
df2024 = conn.read(spreadsheet=bally_2024_url)

df2 = pd.DataFrame(df2025)
print(df2)

col1, col2 = st.columns(2)

with col1:
    st.header("2025 data")
    st.dataframe(df2025)

with col2:
    st.header("2024 data")
    st.dataframe(df2024)




#sql ='''
#        SELECT
#         "F4",
#         "F8"
#        FROM
#          HC
#        WHERE
#          "F4" < 2
#     ''' 
#df3 = conn.query(spreadsheet=url,sql=sql)
#st.dataframe(df3)
#
##側欄、容器測試
#
#map_data = pd.DataFrame(
#    np.random.randn(100, 2) / [50, 50] + [24.0, 120.5],
#    columns=['lat', 'lon'])
#st.sidebar.map((map_data))
#
#with st.container():
#    st.write("This is inside the container")
#
#    # You can call any Streamlit command, including custom components:
#    st.bar_chart(np.random.randn(50, 3))
#    st.scatter_chart(
#        df2,
#        x="Fp1",
#        y=["Fp2","F4"],
#        #color=["#FF0000"]
#        color=["#FF0000", "#0000FF"],
#        )
#
#st.write("This is outside the container")