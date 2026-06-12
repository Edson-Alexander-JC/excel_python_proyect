import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.interfaces.input_item import InputItem

class MacizoRocoso(FabricInterface):
    
    def render_sidebar(self):pass
    def set_vars(self):pass

    def render_view(self):
        st.title("Propiedades del Macizo Rocoso")
        self.make_arquitecture()

    def make_arquitecture(self):
        roc_type = self.ep.print_input(InputItem(
            kind="select", label="tipo de roca", 
            key="roc_type", 
            values= ["1","2","3","4","5","6"]
             
        ))
        roc_pe = self.ep.print_input(InputItem(
            kind="float", key="roc_pe",
            label="peso especifico de la roca", 
        ))

        f_esponjamiento = self.ep.print_input(InputItem(
            kind="float", key="roc_pe",
            label="Factor de esponjamiento del material", 
        ))

    def render(self):
        self.render_sidebar()
        self.render_view()
