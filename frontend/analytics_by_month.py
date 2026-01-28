# import streamlit as st
# from datetime import datetime
# import requests
# import pandas as pd
#
#
# API_URL = "http://localhost:8000"
#
#
# def analytics_months_tab():
#     response = requests.get(f"{API_URL}/monthly_summary/")
#     monthly_summary = response.json()
#
#     df = pd.DataFrame(monthly_summary)
#
#     # Rename columns
#     df.rename(columns={
#         "expense_month": "Month Number",
#         "month_name": "Month Name",
#         "total": "Total"
#     }, inplace=True)
#
#     # Sort months correctly (Jan → Dec)
#     df_sorted = df.sort_values(by="Month Number")
#
#     st.title("Expense Breakdown By Months")
#
#     # ---- BAR CHART ----
#     chart_df = df_sorted.set_index("Month Name")[["Total"]]
#     st.bar_chart(chart_df, use_container_width=True)
#
#     # ---- TABLE ----
#     table_df = df_sorted.set_index("Month Number")
#     table_df["Total"] = table_df["Total"].map("{:.2f}".format)
#
#     st.table(table_df)
import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_months_tab():
    response = requests.get(f"{API_URL}/monthly_summary/")
    monthly_summary = response.json()

    df = pd.DataFrame(monthly_summary)

    # Rename columns
    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total": "Total"
    }, inplace=True)

    # Sort months correctly (Jan → Dec)
    df["Month Number"] = df["Month Number"].astype(int)
    df = df.sort_values(by="Month Number")

    st.title("Expense Breakdown By Months")

    # ================= KPI METRICS =================
    total_expense = df["Total"].sum()
    max_month = df.loc[df["Total"].idxmax(), "Month Name"]

    col1, col2 = st.columns(2)
    col1.metric("Total Expense", f"₹ {total_expense:,.2f}")
    col2.metric("Highest Spending Month", max_month)

    # ================= BAR CHART =================
    st.subheader("Monthly Expense Comparison")
    st.bar_chart(
        df.set_index("Month Name")["Total"],
        use_container_width=True
    )

    # ================= LINE CHART =================
    st.subheader("Monthly Expense Trend")
    st.line_chart(
        df.set_index("Month Name")["Total"],
        use_container_width=True
    )

    # ================= TABLE =================
    table_df = df.copy()
    table_df["Total"] = table_df["Total"].map("{:.2f}".format)

    st.subheader("Monthly Expense Table")
    st.table(table_df.set_index("Month Name"))

    # ================= DOWNLOAD =================
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download Monthly Report",
        csv,
        "monthly_expense_report.csv",
        "text/csv"
    )
