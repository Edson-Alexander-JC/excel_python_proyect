import streamlit as st
from app_module.interfaces.input_item import InputItem
from app_module.interfaces.fabric_interface import FabricInterface

class TaladrosFabric(FabricInterface):
    def set_vars(self):pass
        
    def render_sidebar(self):pass
    
    def diametro(self):
        if(st.session_state["mine_type"]):
            diametro = 230
            largo = 14
            sobre_perfo = 2
        else: 
            diametro = 18
            largo = 4
            sobre_perfo = 0.25
            
    def render_view(self):
        st.subheader("Taladros")
        z_taladro = self.ep.print_input(InputItem(
            key="z_taladro", kind="float", unit="m",
            label="Profundidad del Taladro",
        ))
        diametro_taladro = self.ep.print_input(InputItem(
            key="diametro_taladro", kind="number", unit="mm",
            label="Diametro del Taladro", value=""
        ))
        inclinacion_taladro = self.ep.print_input(InputItem(
            key="inclinacion_taladro", kind="float",
            label="Inclinacion del taladro", unit="º"
        ))
        sobre_perforacion = self.ep.print_input(InputItem(
            key="sobre_perforacion", kind="float",
            label="Sobreperforacion del taladro", unit="m"
        ))
        
        
        
    def make_arquitecture(self):self.render_view()
    