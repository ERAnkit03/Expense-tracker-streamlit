import streamlit as st
import pandas as pd
from db import init_db, add_expense, get_all_expenses
from model import predict_category
import matplotlib.pyplot as plt

init_db()

st.title("AI Expense Tracker")

with st.form("entry_form"):
    date = st.date_input("Date")
    desc = st.text_input("Description")
    amt = st.number_input("Amount", min_value=0.0)
    cat = st.text_input("Category (auto or manual)")

    if st.form_submit_button("Add Expense"):
        predicted = predict_category(desc)
        final_cat = cat if cat else predicted
        add_expense(str(date), desc, amt, final_cat)
        st.success("Expense added!")

df = get_all_expenses()
st.dataframe(df)

if not df.empty:
    cat_totals = df.groupby("category")["amount"].sum()
    fig, ax = plt.subplots()
    cat_totals.plot(kind="bar", ax=ax)
    st.pyplot(fig)
