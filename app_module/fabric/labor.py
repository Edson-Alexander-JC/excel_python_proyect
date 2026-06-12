import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.interfaces.input_item import InputItem

class Labor(FabricInterface):
    def render_sidebar(self):pass
    def set_vars(self):pass

    def render_view(self):
        st.title("Propiedades del Explosivo")
        self.make_arquitecture()

    def make_arquitecture(self):

    def render(self):
        self.render_sidebar()
        self.render_view()
