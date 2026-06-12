import streamlit as st
from app_module.interfaces.input_item import InputItem
from app_module.system.maquinara_mini_forms import MaquinariaMiniForms
from app_module.interfaces.fabric_interface import FabricInterface

class PerforadoraFabric(FabricInterface):
    def set_vars(self):
        self.mini_forms : MaquinariaMiniForms = MaquinariaMiniForms()
        self.mini_forms.set_maquinaria("perforadora")
        
    def render_sidebar(self):pass
    
    def demoras(self):
        self.mini_forms.set_tiempos([
            InputItem(key="change_barras",values=[
                InputItem(value="Cambio/Adicion de barra"),
                InputItem(value=30),
            ]),
            InputItem(key="pos_niv",values=[
                InputItem(value="Posicionamientos y nivelacion"),
                InputItem(value=35),
            ]),
            InputItem(key="change_brocas",values=[
                InputItem(value="Cambio de brocas"),
                InputItem(value=30),
            ]),
            InputItem(key="clean_pozo",values=[
                InputItem(value="Limpieza/Soplado del pozo"),
                InputItem(value=20),
            ]),
        ])
    
    def accesorios(self):
        
        st.header("Accesorios")
        self.mini_forms.set_accesorios([
            InputItem(key="barra_1",values=[
                InputItem(value="Barra (4ft)"),
                InputItem(value=50.0),
            ]),
            InputItem(key="barra_2",values=[
                InputItem(value="Barra (6ft)"),
                InputItem(value=100),
            ]),
            InputItem(key="barra_3",values=[
                InputItem(value="Barra (8ft)"),
                InputItem(value=100),
            ]),
            InputItem(key="broca",values=[
                InputItem(value="Broca"),
                InputItem(value=200),
            ]),
        ])
        
        
    def consumo_energia(self): self.mini_forms.set_energia()
    
    def render_view(self):
        self.demoras()
        self.accesorios()
        self.consumo_energia()
        
        
        
        
    def make_arquitecture(self):self.render_view()
    