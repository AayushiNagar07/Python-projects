import streamlit as st

# ---------------- SESSION INIT ----------------
if "user" not in st.session_state:
    st.session_state.user = None


# ---------------- LOGIN ----------------
def login_screen():
    st.header("Login to GENQAI")

    if st.button("Log in with Google"):
        st.session_state.user = {
            "email": "aayushinagar385@gmail.com",
            "name": "Aayushi Nagar"
        }
        st.success("Logged in successfully!")
        st.rerun()

    st.info("Please login to continue.")


# ---------------- ROUTING ----------------
if st.session_state.user is None:
    login_screen()
    st.stop()


# ---------------- DASHBOARD ----------------
st.title("Dashboard")
st.write("Welcome:", st.session_state.user["email"])

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.write("Logged in as:")
    st.write(st.session_state.user["email"])

    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()