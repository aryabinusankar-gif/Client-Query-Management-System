import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.auth import hash_password, verify
from utils.db_utils import get_conn
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Client Query Management System", layout="wide")

menu = st.sidebar.selectbox("Menu", ["Home", "Register", "Login"])

# HOME PAGE
if menu == "Home":
    st.title("Client Query Management System")
    st.write("A simple application to manage client queries.")

# REGISTER PAGE
if menu == "Register":
    st.header("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["client", "support"])
    if st.button("Register"):
        ok = register_user(username, hash_password(password), role)
        if ok:
            st.success("Registration Successful! Please login.")
        else:
            st.error("Username already exists.")

# LOGIN PAGE
if menu == "Login":
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = get_user_by_username(username)
        if user and verify(password, user[2]):
            st.success(f"Welcome {username} ({user[3]})")
            st.session_state['user'] = {'id': user[0], 'username': user[1], 'role': user[3]}
        else:
            st.error("Invalid credentials.")

# AFTER LOGIN
if st.session_state.get('user'):
    user = st.session_state['user']

    if user['role'] == 'client':
        st.header("Submit Query")
        title = st.text_input("Query Title")
        desc = st.text_area("Query Description")
        if st.button("Submit"):
            conn = get_conn()
            cur = conn.cursor()
            qid = "CQ-" + datetime.utcnow().strftime("%Y%m%d%H%M%S")
            created_at = datetime.utcnow().isoformat()
            cur.execute("""INSERT INTO queries 
                (query_id, user_id, title, description, status, created_at)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (qid, user['id'], title, desc, 'open', created_at))
            conn.commit()
            conn.close()
            st.success(f"Query submitted with ID: {qid}")

    if user['role'] == 'support':
        st.header("All Queries")
        conn = get_conn()
        df = pd.read_sql_query("""
            SELECT q.query_id, u.username, q.title, q.description, q.status, q.created_at
            FROM queries q
            LEFT JOIN users u ON q.user_id = u.id
        """, conn)
        conn.close()

        st.dataframe(df)

        st.subheader("Close a Query")
        qid = st.text_input("Enter Query ID to close")
        if st.button("Close"):
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("UPDATE queries SET status='closed', closed_at=? WHERE query_id=?",
                        (datetime.utcnow().isoformat(), qid))
            conn.commit()
            conn.close()
            st.success("Query closed successfully")