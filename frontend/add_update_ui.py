import requests
import streamlit as st
from datetime import datetime
API_URL = "http://localhost:8000"
categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
def add_update_tab():
    selected_date = st.date_input(
        "Enter date:",
        datetime(2024, 8, 1),
        label_visibility="collapsed"
    )

    selected_date_str = selected_date.strftime("%Y-%m-%d")

    response = requests.get(f"{API_URL}/expenses/{selected_date_str}")

    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retrieve expenses")
        existing_expenses = []

    with st.form(key="expenses_from"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Amount")
        with col2:
            st.subheader("Category")
        with col3:
            st.subheader("Notes")

        Expenses = []

        for i in range(5):
            if i < len(existing_expenses):
                Amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                Amount = 0.0
                category = "Shopping"
                notes = ""

            if isinstance(category, str):
                category = category.capitalize()

            if category not in categories:
                category = "Other"

            col1, col2, col3 = st.columns(3)

            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=1.0,
                    value=float(Amount),
                    key=f"{selected_date_str}_amount_{i}",
                    label_visibility="collapsed"
                )

            with col2:
                category_input = st.selectbox(
                    label="Category",
                    options=categories,
                    index=categories.index(category),
                    key=f"{selected_date_str}_category_{i}",
                    label_visibility="collapsed"
                )

            with col3:
                notes_input = st.text_input(
                    label="notes",
                    value=notes,
                    key=f"{selected_date_str}_notes_{i}",
                    label_visibility="collapsed"
                )

            Expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            filtered_expenses = [e for e in Expenses if e["amount"] > 0.0]

            post_response = requests.post(
                f"{API_URL}/expenses/{selected_date_str}",
                json=filtered_expenses
            )

            if post_response.status_code == 200:
                st.success("Expenses updated successfully ")
            else:
                st.error(f"Failed to update expenses : {post_response.text}")
