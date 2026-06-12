import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface

class Acarreo(FabricInterface):
    
    def set_vars(self):pass

    def render_sidebar(self):
        with st.sidebar:
            st.divider()
            self.burden = st.number_input(
                "Burden",
                min_value=0.0
            )

            self.espaciamiento = st.number_input(
                "Espaciamiento",
                min_value=0.0
            )

    def render_view(self):
        st.title("Acarreo")

        st.write(f"Burden: {self.burden}")
        st.write(f"Espaciamiento: {self.espaciamiento}")

    def make_arquitecture(self):pass
    def render(self):
        self.render_sidebar()
        self.render_view()
