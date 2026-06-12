import streamlit as st
from app_module.interfaces.input_item import InputItem
from app_module.shared.every_put import EveryPut
from app_module.shared.colum_setter import ColumnSetter
from app_module.shared.data_full_verify import DataFullVerify
from app_module.shared.demoras_part import DemorasPart


class TiemposMaquinaria():
    def __init__(self):
        self.ep : EveryPut = EveryPut()
        self.cs : ColumnSetter = ColumnSetter()
        self.dfv : DataFullVerify = DataFullVerify()
    
    def set_maquinaria(self,maq_name):
        self.maq_name = maq_name
        self.my_key = self.maq_name+"_demoras_list"
        self.dp = DemorasPart(self.my_key,maq_name)
    
    def put_demoras_ciclo(self,items=[]):
        label=f"""Demoras del ciclo de la {self.maq_name} (min/turno)"""
        self.dp.make_demoras(label,items)
    
    def horas(self):
        self.ep.print_input(InputItem(
            key=("t_gas_" + self.maq_name), 
            kind="number", value=60,unit="min",
            label="Tiempo de llenado de combustible",
            
        ))
        self.ep.print_input(InputItem(
            key=("mant_corectivo_" + self.maq_name), 
            kind="number", value=60,unit="min/turno",
            label="Mantenimiento correctivo",
            
        ))
        self.ep.print_input(InputItem(
            key=("mant_preventivo" + self.maq_name), 
            kind="number", value=60,unit="min/turno",
            label="Mantenimiento preventivo",
            
        ))
        
    def tiempos(self,items):
        self.cs.mk_col([
            lambda:self.put_demoras_ciclo(items),
            lambda:self.horas(),
        ])
    
    def render_tiempos(self,items): 
        st.subheader("Tiempos")
        self.tiempos(items)
    