import streamlit as st
from app_module.interfaces.input_item import InputItem
from app_module.system.maquinara_mini_forms import MaquinariaMiniForms
from app_module.interfaces.view_interface import ViewInterface
from app_module.shared.button_sidebar_element import ButtonSidebarElement

class ExplosivoFabric(ViewInterface):
    def render_sidebar(self):pass
    def set_vars(self):pass
        
    def render_view(self):
        st.title("Propiedades del Explosivo")
        exp_type = self.ep.print_input(InputItem(
            key="exp_type", kind="select",
            label="tipo explosivo", 
            values=["ANFO","HA","TNT","Dinamita"]
        ))
        
        if(st.session_state.get("exp_type") == "ANFO"):
            self.cs.mk_col([
                lambda: self.ep.print_input(InputItem(
                    key="diesel", kind="float",
                    label="Combustible",
                    value=0.5, unit="%"
                )),
                lambda:self.ep.print_input(InputItem(
                    key="NA", kind="float",
                    label="Nitrato Amonio", 
                    value=0.5, unit="%"
                ))
            ])
            
        self.ep.print_input(InputItem(
            key="costo_exp", kind="float",
            label="Costo del explosivo",
            value=30.0, unit="$/Kg"
        ))
        frente_w = self.ep.print_input(InputItem(
            key="frente_w", kind="float",
            label="peso especifico del explosivo", 
        ))
        frente_h = self.ep.print_input(InputItem(
            key="frente_h", kind="float",
            label="velocidad de detonacion", 
        ))
#kg de anfo 30 dolares

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
        st.subheader("Propiedades de Mineria Superficial")
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
        st.subheader("Propiedades de Mineria Subterranea")
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
