import streamlit as st
st.set_page_config(layout="wide")
from app_module.features.main_sidebar.main_sidebar import MainSideBar
MainSideBar().render()