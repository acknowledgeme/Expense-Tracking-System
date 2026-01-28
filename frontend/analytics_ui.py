# import requests
# import streamlit as st
# import pandas as pd
# from datetime import datetime
# API_URL = "http://localhost:8000"
# def analytics_tab():
#     col1,col2=st.columns(2)
#     with col1:
#         start_date=st.date_input("Start Date",datetime(2024,8,1))
#     with col2:
#         end_date=st.date_input("End Date",datetime(2024,8,5))
#     if st.button("get_Analytics"):
#         payload = {
#             "start_date":start_date.strftime("%Y-%m-%d"),
#             "end_date":end_date.strftime("%Y-%m-%d"),
#         }
#         response=requests.get(f"{API_URL}/analytics/",json=payload)
#         response=response.json
#
#         data={
#             "category":list(response.keys()),
#             "Total":[response[category]["total"] for category in response],
#             "percentage":[response[category]["percentage"] for category in response]
#         }
#         df=pd.DataFrame(data)
#         df.sorted=df.sort_values(by="Percentage",ascending=False)
#         st.table(df)
# import requests
# import streamlit as st
# import pandas as pd
# from datetime import datetime
#
# API_URL = "http://localhost:8000"
#
# def analytics_tab():
#     col1, col2 = st.columns(2)
#
#     with col1:
#         start_date = st.date_input("Start Date", datetime(2024, 8, 1))
#     with col2:
#         end_date = st.date_input("End Date", datetime(2024, 8, 5))
#
#     if st.button("Get Analytics"):
#         payload = {
#             "start_date": start_date.strftime("%Y-%m-%d"),
#             "end_date": end_date.strftime("%Y-%m-%d"),
#         }
#
#         # FIX: use POST instead of GET
#         response = requests.post(f"{API_URL}/analytics/", json=payload)
#
#         if response.status_code == 200:
#             response = response.json()
#
#             data = {
#                 "category": list(response.keys()),
#                 "total": [response[c]["total"] for c in response],
#                 "percentage": [response[c]["percentage"] for c in response]
#             }
#
#             df = pd.DataFrame(data)
#             df = df.sort_values(by="percentage", ascending=False)
#
#             st.table(df)
#
#         else:
#             st.error(f"Error: {response.status_code}")
#             st.write(response.text)
import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)
        response = response.json()

        data = {
            "Category": list(response.keys()),
            "Total": [response[category]["total"] for category in response],
            "Percentage": [response[category]["percentage"] for category in response]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.title("Expense Breakdown By Category")

        #FIX HERE
        st.bar_chart(df_sorted.set_index("Category")["Percentage"], use_container_width=True)

        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.table(df_sorted)
def analytics_months_tab():
    response = requests.get(f"{API_URL}/monthly_summary/")

    if response.status_code != 200:
        st.error("Failed to fetch monthly summary")
        return

    monthly_summary = response.json()

    if not monthly_summary:
        st.warning("No monthly data available")
        return

    # EXPLICIT COLUMN NAMES (THIS WAS THE MISSING PIECE)
    df = pd.DataFrame(
        monthly_summary,
        columns=["expense_month", "month_name", "total"]
    )

    df_sorted = df.sort_values(by="expense_month")

    st.title("Expense Breakdown By Months")

    # ---- BAR CHART ----
    st.bar_chart(
        df_sorted.set_index("month_name")[["total"]],
        use_container_width=True
    )

    # ---- TABLE ----
    table_df = df_sorted.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total": "Total"
    })

    table_df["Total"] = table_df["Total"].map("{:.2f}".format)

    st.table(table_df[["Month Number", "Month Name", "Total"]])
