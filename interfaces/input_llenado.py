import streamlit as st
from interfaces.data_interfaces.input_item import InputItem
from collections.abc import Callable

class InputLlenado:
    def __init__(self, input: InputItem | None = None):
        if input is None:
            input = InputItem(
                "item_llenado",
                value=InputItem("input_llenado"),
                values=[]
            )
        input_set:InputItem = input.value
        items_default:list = input.values.copy()
        
        self.my_list:InputItem = input 
        self.inputs:InputItem = input_set
        self.items:list = items_default or []

    def add(self)->None:
        nuevo_item = InputItem(
            key=self.my_input.key,
            values=self.my_input.values,
        )
        self.items.append(nuevo_item)
    
    def remove(self)->None:
        key = st.session_state["item_index"]
        if key != None:
            for indice, item in enumerate(self.items):
                if item.key == key: 
                    del self.items[indice]
            
                    if st.session_state["item_index"] == key:
                        st.session_state["item_index"] = None
                    break
                    
    def revert(self):
        items_unicos = {}
        for item in self.items + self.my_input.values:
            items_unicos[item.key] = item

        self.items = list(items_unicos.values())

    def select_item(self,key:str): 
        if st.session_state["item_index"] == key:
            st.session_state["item_index"] = None
        else:    st.session_state["item_index"] = key
        
    def print_outputs(self):
        #Elementos:
        with st.container(boder=True):
            #estos son los outputs predeterminados y que se pueden seleccionar
            for item in self.items:
                if st.session_state["item_index"] == item.key:
                    border = "3px solid #1f77b4"
                    background = "#e8f0fe"
                else:
                    border = "1px solid #cccccc"
                    background = "#ffffff"

                st.markdown(f"""<div style="
                    border: {border};
                    background-color: {background};
                ">""", unsafe_allow_html=True)
                
                texto = " | ".join(str(v.value) for v in item.values)
                if not texto: texto = str(item.value)
                
                if st.button(
                    texto,
                    key=item.key,
                    use_container_width=True,
                ):
                    self.select_item(item.key)

                st.markdown("</div>", unsafe_allow_html=True)
                

        
        