import streamlit as st

st.set_page_config(page_title="TRACK-MY-VOYAGE", layout="wide")

st.title("🚢 TRACK-MY-VOYAGE")

st.markdown("""
Welcome to **TRACK-MY-VOYAGE** — a tool to detect ships from satellite images using advanced AI detection.

Click below to get started!
""")

# This creates a link in Streamlit's sidebar for navigation
st.page_link("pages/Detect_Ships.py", label="🛰️ Detect Ships", icon="🧭")
