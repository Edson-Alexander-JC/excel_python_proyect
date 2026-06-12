import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.interfaces.input_item import InputItem

class FrenteVoladura(FabricInterface):
    def render_sidebar(self):pass
    def set_vars(self):pass
        
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
        st.title("Propiedades del Frente de Voladura")
        self.make_arquitecture()

    def make_arquitecture(self):
        self.general_propertis()
        if(st.session_state["mine_type"]):
            self.subterraneo_properties()
        else:
            self.superficial_properties()

    def general_propertis(self):
        frente_w = self.ep.print_input(InputItem(
            key="frente_w", kind="float",
            label="peso especifico del explosivo", 
        ))
        frente_h = self.ep.print_input(InputItem(
            key="frente_h", kind="float",
            label="velocidad de detonacion", 
        ))
        
        


    def superficial_properties(self):
        frente_sup_type = self.ep.print_input(InputItem(
            key="frente_sup_type", kind="radio",
            label="Seleccione tipo de Banco",
            values=["Vertical", "Inclinada", "En cuña"] 
        ))
        angulo_talud = self.ep.print_input(InputItem(
            key="angulo_talud", kind="float",
            label="Coloque el angulo de Talud",
        ))
        banco_altura = self.ep.print_input(InputItem(
            key="banco_altura", kind="float",
            label="Coloque la altura del banco",
        ))
    
    def subterraneo_properties(self):
        frente_sub_type = self.ep.print_input(InputItem(
            key="frente_sub_type", kind="radio",
            label="Seleccione tipo de seccion",
            values=["Semicircular", "Baúl", "Rectangular"] 
        ))
        z_labor = self.ep.print_input(InputItem(
            key="banco_altura", kind="float",
            label="Coloque la profundidad de la labor",
        ))
    

    def render(self):
        self.render_sidebar()
        self.render_view()
