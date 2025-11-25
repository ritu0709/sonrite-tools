import streamlit as st

st.title("SonRite – Pump Assessment")

flow = st.number_input("Flow (m³/h)", 0.0, 10000.0, 100.0)
head = st.number_input("Head (m)", 0.0, 200.0, 40.0)

st.write("This is your first SonRite tool!")