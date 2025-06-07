import streamlit as st
from RandPassGen import generate_password

st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")
st.title("🔐 Password Generator")

# Sidebar options
length = st.sidebar.number_input("Password Length", min_value=4, max_value=100, value=12, step=1)
include_upper = st.sidebar.checkbox("Include Uppercase Letters", value=True)
include_lower = st.sidebar.checkbox("Include Lowercase Letters", value=True)
include_digits = st.sidebar.checkbox("Include Numbers", value=True)
include_symbols = st.sidebar.checkbox("Include Symbols", value=False)

if st.button("Generate Password"):
    password = generate_password(length, include_upper, include_lower, include_digits, include_symbols)
    if "⚠️" in password:
        st.warning(password)
    else:
        st.success("Here is your password:")
        st.code(password)
