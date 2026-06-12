import streamlit as st
from app_module.shared.sidebar import SideBar
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.fabric.acarrero import Acarreo
from app_module.interfaces.input_item import InputItem

from app_module.domain.mina_forms import MinaForms

#Elements
from .elements.roca_fabric import RocaEsterilFabric
from .elements.mineral_fabric import MineralFabric
from ..labor.labor_fabric import LaborFabric

class MainSideBar(FabricInterface):
    def view_arquitecture(self):pass
    def header(self):pass
    def inicio(self):pass
    
    
    def render_sidebar(self):
        with st.sidebar:
            with st.container(border=True,horizontal_alignment="center"):
                estado = st.session_state.get("mine_type",False)
                texto = "Subterranea" if estado else "Superficial"
                st.toggle(texto, key="mine_type")
            
            LaborFabric().render_sidebar()
            RocaEsterilFabric().render_sidebar()
            MineralFabric().render_sidebar()

        pages = MinaForms.get_forms()
        
        self.my_sidebar.def_pages(pages)
        self.my_sidebar.render_sidebar("Seleccione un formulario")
        
    def set_vars(self,):
        self.my_sidebar = SideBar()
    
    def render_view(self):
        self.my_sidebar.render_view()

    def make_arquitecture(self): 
        self.render_sidebar()
        self.render_view()
        
    
        