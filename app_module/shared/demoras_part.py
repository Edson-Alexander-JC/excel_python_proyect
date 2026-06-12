import streamlit as st
from app_module.interfaces.input_item import InputItem
from app_module.shared.every_put import EveryPut
from app_module.shared.colum_setter import ColumnSetter
from app_module.shared.data_full_verify import DataFullVerify

class DemorasPart():
    def __init__(self,key,maq_name):
        self.my_key = key
        self.ep = EveryPut()
        self.maq_name = maq_name
        
    def make_demoras(self,label="",items=[]):
        self.component = self.ep.print_input(InputItem(
            kind="list",key=self.my_key,
            label=label,
            value=InputItem(values=[
                InputItem(
                    label="concepto de la demora",
                    key=("concepto_"+self.maq_name),kind="string"
                ),
                InputItem(
                    label="tiempo", key=("demoras_"+self.maq_name),
                    kind="number",unit="min"
                ),
            ]),
            values=items
            )
        )
    
    def get_sumatoria(self):
        num = self.component.sumatoria_filtrado("demoras_"+self.maq_name)
        if not num: num = 0
        return  num