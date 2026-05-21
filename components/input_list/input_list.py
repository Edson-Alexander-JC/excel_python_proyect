from pathlib import Path
import streamlit as st

class InputList():
    def __init__(self):
        self.path:str="components/input_list/input_list"
        self.input_list_component = st.components.v2.component(
            "interactive_counter",
            html=Path(self.path + ".html").read_text(encoding="utf-8"),
            css=Path(self.path + ".css").read_text(encoding="utf-8"),
            js=Path(self.path + ".js").read_text(encoding="utf-8"),
        )
        
        result = self.input_list_component(
            default={"count": 0},
            data={"initialCount": 0},
            on_count_change=lambda: None,
            on_reset_change=lambda: None,
        )
