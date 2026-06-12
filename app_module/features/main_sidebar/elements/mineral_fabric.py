import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.interfaces.input_item import InputItem
from app_module.shared.button_sidebar_element import ButtonSidebarElement
from app_module.fabric.geomecanica_fabric import GeomecanicaFabric

class MineralFabric(FabricInterface):
    def set_vars(self):
        pass
    def render_sidebar(self):
        
        with st.expander("MINERAL"):pass

    def render_view(self):
        pass            
    def make_arquitecture(self):pass
    
    