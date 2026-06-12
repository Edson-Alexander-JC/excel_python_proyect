import streamlit as st
from app_module.interfaces.input_item import InputItem
from app_module.system.maquinara_mini_forms import MaquinariaMiniForms
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.shared.button_sidebar_element import ButtonSidebarElement
#FORMS
from .forms.perforadora import PerforadoraFabric
from .forms.taladros import TaladrosFabric

class Perforacion(FabricInterface):
    def set_vars(self):
        self.btns = ButtonSidebarElement("perforacion_buttons")
        self.pages = {
            "index" : PerforadoraFabric(),
            "perforadora_view" : PerforadoraFabric(),
            "taladros_view" : TaladrosFabric(),
        }
        
    def render_sidebar(self):
        self.btns.put_button("Perforadora","perforadora_view")
        self.btns.put_button("Taladros","taladros_view")
    
    def render_view(self):
        self.pages[self.btns.get_index()].render_view()
        
    def make_arquitecture(self):pass
    