# import requests
# import streamlit as st
# from datetime import datetime
#
#
# API_URL='http://localhost:8000'
#
# st.title("Expense Tracking System")
# tab1,tab2=st.tabs(['Add/Update','Analytics'])
#
# with tab1:
#     selected_date=st.date_input("Enter date:",datetime(2024,8,1),label_visibility="collapsed")
#     response=requests.get(f"{API_URL}/expenses/{selected_date}")
#
#     if response.status_code==200:
#         existing_expenses=response.json()
#         st.write(existing_expenses)
#     else:
#         st.error("failed to retrive expenses")
#         existing_expenses=[]
# with tab1:
#     selected_date = st.date_input(
#         "Enter date:",
#         datetime(2024, 8, 1),
#         label_visibility="collapsed"
#     )
#
#     response = requests.get(f"{API_URL}/expenses/{selected_date}")
#     if response.status_code == 200:
#         existing_expenses = response.json()
#     else:
#         st.error("Failed to retrieve expenses")
#         existing_expenses = []
# categories=["Rent","Food","Shopping","Entertainment","Other"]
# with st.form(key="expenses_from"):
#     col1,col2,col3=st.columns(3)
#     with col1:
#         st.subheader("Amount")
#     with col2:
#         st.subheader("Category")
#     with col3:
#         st.subheader("Notes")
#     for i in range(5):
#         if i<len(existing_expenses):
#             Amount=existing_expenses[i]["amount"]
#             category=existing_expenses[i]["category"]
#             notes=existing_expenses[i]["notes"]
#         else:
#             Amount=0.0
#             category="Shopping"
#             notes=""
#
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.number_input(label="Amount",min_value=0.0,step=1.0,value=Amount,key=f"amount_{i}",label_visibility="collapsed")
#         with col2:
#             st.selectbox(label='Category',options=categories,index=categories.index(category), key=f"category_{i}",label_visibility="collapsed")
#         with col3:
#            notes_input=st.text_input(label="notes",value=notes,key=f"notes_{i}",label_visibility="collapsed")
#     submit_button=st.form_submit_button()
#     if submit_button:
#         pass

# import requests
# import streamlit as st
# from datetime import datetime
#
# API_URL = "http://localhost:8000"
#
# st.title("Expense Tracking System")
# tab1, tab2 = st.tabs(["Add/Update", "Analytics"])
#
# categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
#
# with tab1:
#     selected_date = st.date_input(
#         "Enter date:",
#         datetime(2024, 8, 1),
#         label_visibility="collapsed"
#     )
#
#     # ✅ Convert to backend required format
#     selected_date_str = selected_date.strftime("%Y-%m-%d")
#
#     # ✅ Fetch expenses from backend
#     response = requests.get(f"{API_URL}/expenses/{selected_date_str}")
#
#     if response.status_code == 200:
#         existing_expenses = response.json()
#         # st.write(existing_expenses)  # optional debug
#     else:
#         st.error("Failed to retrieve expenses")
#         existing_expenses = []
#
#     # ✅ FORM (same as your style)
#     with st.form(key="expenses_from"):
#         col1, col2, col3 = st.columns(3)
#
#         with col1:
#             st.subheader("Amount")
#         with col2:
#             st.subheader("Category")
#         with col3:
#             st.subheader("Notes")
#         Expenses=[]
#         for i in range(5):
#             if i < len(existing_expenses):
#                 Amount = existing_expenses[i]["amount"]
#                 category = existing_expenses[i]["category"]
#                 notes = existing_expenses[i]["notes"]
#             else:
#                 Amount = 0.0
#                 category = "Shopping"
#                 notes = ""
#
#             # ✅ Fix category mismatch like "shopping" -> "Shopping"
#             if isinstance(category, str):
#                 category = category.capitalize()
#
#             if category not in categories:
#                 category = "Other"
#
#             col1, col2, col3 = st.columns(3)
#
#             # ✅ IMPORTANT FIX: Keys must depend on date also
#             with col1:
#                amount_input= st.number_input(
#                     label="Amount",
#                     min_value=0.0,
#                     step=1.0,
#                     value=float(Amount),
#                     key=f"{selected_date_str}_amount_{i}",
#                     label_visibility="collapsed"
#                 )
#
#             with col2:
#                 category_input=st.selectbox(
#                     label="Category",
#                     options=categories,
#                     index=categories.index(category),
#                     key=f"{selected_date_str}_category_{i}",
#                     label_visibility="collapsed"
#                 )
#
#             with col3:
#                 notes_input = st.text_input(
#                     label="notes",
#                     value=notes,
#                     key=f"{selected_date_str}_notes_{i}",
#                     label_visibility="collapsed"
#                 )
#             Expenses.append({
#                 "Amount":amount_input,
#                 "Category":category_input,
#                 "Notes":notes_input
#             })
#
#         submit_button = st.form_submit_button()
#
#         if submit_button:
#             filtered_expenses=[expense for expense in Expenses if expense["Amount"] > 0.0]
#             requests.post(f"{API_URL}/expenses/{selected_date_str}", json=filtered_expenses)
#             if response.status_code==200:
#                 st.success("Expenses updated successfully")
#             else:
#                 st.error("Failed to update expenses")

import requests
import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from analytics_ui import analytics_months_tab
API_URL = "http://localhost:8000"

st.title("Expense Tracking System")
tab1, tab2,tab3 = st.tabs(["Add/Update", "Analytics","Analytics_By_Months"])



with tab1:
    add_update_tab()
with tab2:
    analytics_tab()
with tab3:
    analytics_months_tab()

