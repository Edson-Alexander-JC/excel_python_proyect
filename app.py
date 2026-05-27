import streamlit as st
st.set_page_config(layout="wide")
from tests.fabric_test import FabricTest
from fabric.voladura_fabric import VoladuraFabric

VoladuraFabric()