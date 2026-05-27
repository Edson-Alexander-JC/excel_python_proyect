import streamlit as st
from data.input_item import InputItem
from collections.abc import Callable
from components.input_list.input_list import InputList
import streamlit.components.v1 as components

class EveryPut:
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
            case "radio":
                resultado = st.radio(label,item.values)
            case _: 
                return st.warning("Tipo no soportado: " + item.kind)
        
        return resultado
    
    def def_inputs(self, item: InputItem):
        value = None
        if item.unit != "":
            col1, col2 = st.columns([4, 1])
            
            with col1: value = self.print_input(item)
            with col2:
                st.markdown(f"""<div 
                    style='
                        height:60px;
                        display:flex;
                        align-items: flex-end;
                        justify-content: flex-start;
                    '    
                >
                    {item.unit}
                </div>""", unsafe_allow_html=True)
        else:
            value = self.print_input(item)
        return value
    
    def print_output(self, item: InputItem):
        valor = item.value
        unidad = item.unit
        label = item.label

        label_html = ""
        unit_html = ""

        # LABEL
        if label:
            label_html = f"""
            <div style="
                padding:0 12px;
                background:#1c1f26;
                border-right:1px solid #555;

                display:flex;
                align-items:center;

                white-space:nowrap;
            ">
                {label}
            </div>
            """

        # UNIT
        if unidad:
            unit_html = f"""
            <div style="
                padding:0 12px;
                background:#1c1f26;
                border-left:1px solid #555;

                display:flex;
                align-items:center;

                white-space:nowrap;
            ">
                {unidad}
            </div>
            """

        html = f"""
        <div style="
            display:flex;
            align-items:stretch;

            border:1px solid #555;
            border-radius:8px;

            overflow:hidden;
            height:40px;

            background:#0e1117;
        ">

            {label_html}

            <div style="
                flex:1;
                padding:0 12px;

                display:flex;
                align-items:center;
            ">
                {valor}
            </div>

            {unit_html}

        </div>
        """

        st.html(html)