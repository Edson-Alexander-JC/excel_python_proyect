from dataclasses import dataclass, field, asdict
from data.input_item import InputItem
from pathlib import Path
import streamlit as st
@dataclass
class InputList():
    def __init__(self,data:InputItem):
        self.component = st.components.v2.component(
            "input_list",
            html=Path("components/input_list/input_list.html").read_text(encoding="utf-8"),
            css=Path("components/input_list/input_list.css").read_text(encoding="utf-8"),
            js=Path("components/input_list/input_list.js").read_text(encoding="utf-8"),
        )        
        self.data = data
        return self.component(data=data)
    
    # item = InputItem(
    #             kind = "list",
    #             key= "inputlist",
    #             label ="lista de prueba",
    #             #inputs_row
    #             value = InputItem(kind = "inputs",key= "inputs",
    #                 values= [
    #                     InputItem(kind = "number",key= "number"),
    #                     InputItem(kind = "checkbox",key= "checkbox"),
    #                     InputItem(kind = "text",key= "text2"),
    #                 ]   
    #             ),
    #             #outputs_default
    #             values= [
    #                 InputItem(key= "rpta1",values=[
    #                     InputItem(value="156"),
    #                     InputItem(value="true"),
    #                     InputItem(value="asdsa"),
    #                 ]),
    #                 InputItem(key= "rpta2",values=[
    #                     InputItem(value="156"),
    #                     InputItem(value="true"),
    #                     InputItem(value="asdsa"),
    #                 ]),
    #             ]
    #         );