import streamlit as st
import pandas as pd

st.title("Daromad bo'yicha Qo'shma Shtatlardagi eng yirik kompaniyalar ro'yxati")

data = pd.read_csv('python_darslari\python_darslari\python_ai\Company.csv')

view = st.sidebar.radio(
    "Ma'lumotni qay tarzda ko'rmoqchisiz",
    ("To'liq",'Top 5 ta','Top 10 ta','Top 20 ta')
)

if view == "To'liq":
    st.subheader("To'liq ma'lumot")
    st.dataframe(data)

elif view == "Top 5 ta":
    st.subheader("Top 5 ta")
    st.dataframe(data.head(5))

elif view == "Top 10 ta":
    st.subheader("Top 10 ta")
    st.dataframe(data.head(10))

elif view == "Top 20 ta":
    st.subheader("Top 20 ta")
    st.dataframe(data.head(20))