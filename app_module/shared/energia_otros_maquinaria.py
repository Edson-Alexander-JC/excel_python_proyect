import streamlit as st
from app_module.interfaces.input_item import InputItem
from app_module.shared.every_put import EveryPut
from app_module.shared.colum_setter import ColumnSetter
from app_module.shared.data_full_verify import DataFullVerify

class EnergiaOtrosMaquinaria():
    def __init__(self):
        self.ep : EveryPut = EveryPut()
        self.cs : ColumnSetter = ColumnSetter()
        self.dfv : DataFullVerify = DataFullVerify()
        
    def set_maquinaria(self,maq_name):
        self.maq_name = maq_name
    def def_energia(self):
        st.session_state["energy_type_perforadora"] = self.ep.print_input(InputItem(
            key="energy_type_"+self.maq_name, kind="radio",
            label="Tipo de energia de uso: ",
            values=["Gasolina","Electricidad"]
        ))
        
        self.energia = st.session_state["energy_type_"+self.maq_name]
        self.unit = ""
        
        if self.energia == "Gasolina":
            self.unit = "gal/h"
        else: self.unit = "Kw/h"
        
    def render_energia(self,energia=0,lubricante=0,aceite=0):
        st.divider()
        st.subheader("Consumo de Energia, Lubricante y Aceite")
        
        self.cs.mk_col([
            lambda: self.def_energia(),
            lambda: self.ep.print_input(InputItem(
                key="energia_"+self.maq_name, 
                kind="float", unit=self.unit,
                label=self.energia, value=energia
            )),
            lambda: self.ep.print_input(InputItem(
                key="lubricante_"+self.maq_name, 
                kind="float", unit="gal/h",
                label="Lubricante", value=lubricante
            )),
            lambda: self.ep.print_input(InputItem(
                key="aceite_"+self.maq_name, 
                kind="float", unit="gal/h",
                label="Aceite", value=aceite
            )),
        ])
