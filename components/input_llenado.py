import streamlit as st
from data.input_item import InputItem
from collections.abc import Callable
from components.input_list.input_list import InputList
import streamlit.components.v1 as components


class InputLlenado:
    def get_label(self, item): 
        if item.label and item.label.strip(): 
            return item.label, "visible" 
        return "label", "collapsed" 
    
    def get_unit(self,item:InputItem): 
        if item.unit: 
            st.markdown( f""" 
                <div style=" 
                background-color:#666; 
                font-size: 18px; color: #666; 
                "> {item.unit} 
                </div> """, 
                unsafe_allow_html=True, 
            );
        
        
    def print_input(self,item:InputItem): 
        label, visibility = self.get_label(item)
        match item.kind: 
            case "string": 
                resultado = st.text_input( 
                        label,label_visibility=visibility, 
                        value=item.value or "", key=item.key
                    ) 
            case "number": 
                resultado = st.number_input( 
                        label,label_visibility=visibility, min_value=0,step=1, 
                        value=item.value or 0, key=item.key
                    ) 
            case "float": 
                resultado = st.number_input(
                        label,label_visibility=visibility, min_value=0.0, 
                        value=item.value or 0.0,format="%.2f", key=item.key 
                    ) 
            case "select": 
                resultado = st.selectbox( 
                        label, item.values, 
                        label_visibility=visibility, index=0, key=item.key 
                    ) 
            case "list": 
                resultado = InputList(item)
            case "bool": 
                resultado = st.checkbox( 
                        label,label_visibility=visibility, 
                        value=item.value if item.value is not None else False, key=item.key 
                    ) 
            case _: 
                return st.warning("Tipo no soportado: " + item.kind)
        
        return resultado
    
    def def_inputs(self, item: InputItem):
        if item.unit != "":
            col1, col2 = st.columns([4, 1])
            
            with col1: self.print_input(item)
            with col2:
                st.markdown(
                    f"<div style='line-height: 2.5rem;'>{item.unit}</div>", 
                    unsafe_allow_html=True
                )
        else:
            self.print_input(item)