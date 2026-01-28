from contextlib import contextmanager
import mysql.connector
from logging_setup import set_up_logger
logger=set_up_logger("db_helper")

@contextmanager
def get_db_cursor(dictionary=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )
    cursor = connection.cursor(dictionary=dictionary)
    try:
        yield cursor
        connection.commit()
    finally:
        cursor.close()
        connection.close()

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses=cursor.fetchall()
        for expense in expenses:
            print(expense)
def fetch_all_expenses_for_date(expense_date):
    logger.info(f"fetch_all_expenses_for_date:{expense_date}")
    with get_db_cursor(dictionary=True) as cursor:
        cursor.execute(
            "SELECT * FROM expenses WHERE expense_date=%s",
            (expense_date,)
        )
        return cursor.fetchall()

def delete_all_expenses_for_date(expense_date):
    logger.info(f"delete_all_expenses_for_date:{expense_date}")
    with get_db_cursor(dictionary=True) as cursor:
        cursor.execute(
            "DELETE FROM expenses WHERE expense_date=%s",(expense_date,)
        )
def insert_expense(expense_date,amount,category,notes):
    logger.info(f"insert_expense:{expense_date},{amount},{category},{notes}")
    with get_db_cursor() as cursor:
        cursor.execute("INSERT INTO expenses(expense_date,amount,category,notes) VALUES(%s,%s,%s,%s)",(expense_date,amount,category,notes))
# def fetch_expense_summary(start_date,end_date):
#     logger.info(f"fetch_expense_summary:{start_date},{end_date}")
#     with get_db_cursor() as cursor:
#         cursor.execute(
#             '''SELECT category,SUM(amount) FROM expenses
#                WHERE expense_date BETWEEN %s AND %s
#                 GROUP BY category''',(start_date,end_date))
#
#         data=cursor.fetchall()
#         return data
def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary:{start_date},{end_date}")

    with get_db_cursor() as cursor:
        cursor.execute(
            """
            SELECT category, SUM(amount) as total
            FROM expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category
            """,
            (start_date, end_date)
        )

        data = cursor.fetchall()

        result = []
        for category, total in data:
            result.append({
                "category": category,
                "total": float(total)
            })

        return result
def fetch_monthly_expense_summary():
    logger.info(f"fetch_expense_summary_by_months")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT month(expense_date) as expense_month, 
               monthname(expense_date) as month_name,
               sum(amount) as total FROM expenses
               GROUP BY expense_month, month_name;
            '''
        )
        data = cursor.fetchall()
        return data


if __name__=="__main__":
    summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    for item in summary:
        print(item)
