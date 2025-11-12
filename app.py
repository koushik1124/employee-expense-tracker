import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Employee Expense Tracker", layout="wide")
st.title("💼 Employee Expense Tracker Dashboard")
st.caption("Built with Streamlit + MySQL | By Koushik Yadagiri")

# ------------------ LOAD ENV VARIABLES ------------------
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "expense_tracker")

# ------------------ VALIDATE ENV CONFIG ------------------
if not all([DB_USER, DB_PASS, DB_NAME]):
    st.error("⚠️ Missing database configuration. Please check your .env file.")
    st.stop()

# ------------------ DATABASE CONNECTION ------------------
try:
    db_url = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(db_url)
except Exception as e:
    st.error(f"Database connection failed ❌: {e}")
    st.stop()

# ------------------ LOAD DATA ------------------
@st.cache_data
def load_data():
    query = """
    SELECT e.name, e.department, x.category, x.amount, x.expense_date
    FROM expenses x
    JOIN employees e ON e.emp_id = x.emp_id
    ORDER BY x.expense_date DESC;
    """
    df = pd.read_sql(query, engine)
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Failed to fetch data: {e}")
    st.stop()

# ------------------ METRICS ------------------
st.markdown("### 📈 Summary Overview")
col1, col2, col3 = st.columns(3)

total_expense = df["amount"].sum()
unique_employees = df["name"].nunique()
departments = df["department"].nunique()

col1.metric("💰 Total Expenses", f"₹{total_expense:,.2f}")
col2.metric("👨‍💼 Employees", unique_employees)
col3.metric("🏢 Departments", departments)

# ------------------ DEPARTMENT SUMMARY ------------------
st.markdown("### 🏢 Department-wise Expense Summary")
summary_query = """
SELECT e.department, SUM(x.amount) AS total_expense
FROM expenses x
JOIN employees e ON e.emp_id = x.emp_id
GROUP BY e.department;
"""
try:
    summary_df = pd.read_sql(summary_query, engine)
    colA, colB = st.columns(2)
    with colA:
        st.dataframe(summary_df, use_container_width=True)
    with colB:
        st.bar_chart(summary_df.set_index("department"))
except Exception as e:
    st.warning(f"Could not load summary chart: {e}")

# ------------------ EXPENSE TABLE ------------------
st.markdown("### 📋 All Expenses")
st.dataframe(df, use_container_width=True)

# ------------------ FILTERS ------------------
st.markdown("### 🔍 Filter by Department")
departments = ["All"] + sorted(df["department"].unique().tolist())
selected_dept = st.selectbox("Select Department", departments)

if selected_dept != "All":
    filtered_df = df[df["department"] == selected_dept]
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)

# ------------------ REFRESH BUTTON ------------------
if st.button("🔄 Refresh Data"):
    st.cache_data.clear()
    st.experimental_rerun()

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("Secure connection via `.env` | Streamlit + SQL Integration")
