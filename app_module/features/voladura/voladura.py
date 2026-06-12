import streamlit as st
from app_module.interfaces.input_item import InputItem
from app_module.system.maquinara_mini_forms import MaquinariaMiniForms
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.shared.button_sidebar_element import ButtonSidebarElement
#FORMS
from .forms.frente_voladura import FrenteVoladuraFabric
from .forms.explosivo import ExplosivoFabric

class Voladura(FabricInterface):
    def set_vars(self):
        self.btns = ButtonSidebarElement("voladura_buttons")
        self.pages = {
            "index" : FrenteVoladuraFabric(),
            "frente_voladura" : FrenteVoladuraFabric(),
            "explosivo" : ExplosivoFabric(),
        }
        
    def render_sidebar(self):
        self.btns.put_button("Frente de Voladura","frente_voladura")
        self.btns.put_button("Explosivos","explosivo")
    
    def render_view(self):
        self.pages[self.btns.get_index()].render_view()
        
    def make_arquitecture(self):pass
    