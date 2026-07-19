import streamlit as st

from auth.login import login_page
from dashboards.customer_dashboard import customer_dashboard
from dashboards.manager_dashboard import manager_dashboard
from dashboards.admin_dashboard import admin_dashboard


st.set_page_config(

    page_title="Axis Bank Dashboard",

    layout="wide"

)


if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "role" not in st.session_state:

    st.session_state.role = ""

if "username" not in st.session_state:

    st.session_state.username = ""


if not st.session_state.logged_in:

    login_page()

else:

    if st.session_state.role == "customer":

        customer_dashboard()

    elif st.session_state.role == "manager":

        manager_dashboard()

    elif st.session_state.role == "admin":

        admin_dashboard()