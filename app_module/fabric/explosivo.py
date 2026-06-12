import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.interfaces.input_item import InputItem

class Explosivo(FabricInterface):
    def render_sidebar(self):pass
    def set_vars(self):pass

    def render_view(self):
        st.title("Propiedades del Explosivo")
        self.make_arquitecture()

    def make_arquitecture(self):
        exp_type = self.ep.print_input(InputItem(
            key="exp_type", kind="float",
            label="peso especifico del explosivo", 
        ))
        exp_pe = self.ep.print_input(InputItem(
            key="exp_pe", kind="float",
            label="peso especifico del explosivo", 
        ))
        vod = self.ep.print_input(InputItem(
            kind="float", key="vod",
            label="velocidad de detonacion", 
        ))

    def render(self):
        self.render_sidebar()
        self.render_view()
