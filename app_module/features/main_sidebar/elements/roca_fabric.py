import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.interfaces.input_item import InputItem
from app_module.shared.demoras_global import DemorasGlobal
from app_module.shared.button_sidebar_element import ButtonSidebarElement
from app_module.fabric.geomecanica_fabric import GeomecanicaFabric

class RocaEsterilFabric(FabricInterface):
    def set_vars(self):
        self.my_items = ButtonSidebarElement("geomecanica_buttons")
        self.pages = {
            "geomecanica" : GeomecanicaFabric(),
        }

    def render_sidebar(self):
        
        with st.expander("ROCA"):
            
            self.cs.mk_col([
                lambda: self.ep.print_input(InputItem(
                    label="Peso especifico",
                    key="esteril_pe", kind="float",
                    value=2.7, unit="t/m³"
                )),
                lambda: self.ep.print_input(InputItem(
                    label="Factor esponjamiento",
                    key="esteril_f_esponjamiento", 
                    kind="float", value=2.7,
                ))
            ])
            
            if(st.session_state["mine_type"]):
                self.my_items.put_button("Geomecanica","geomecanica")

    def render_view(self):
        page = self.my_items.get_index()
        if page:
            self.pages[page].render_view()
            
    def make_arquitecture(self):pass
    
    