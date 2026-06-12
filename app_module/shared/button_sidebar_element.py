import streamlit as st
class ButtonSidebarElement():
    def __init__(self, global_key: str):
        self.global_key = global_key
        if self.global_key not in st.session_state:
            st.session_state[self.global_key] = None
            
    def put_button(self,btn_name,value):
        if st.button(btn_name,use_container_width=True):
            st.session_state[self.global_key] = value
            st.rerun()
            
    def get_index(self):
        if not st.session_state.get(self.global_key): return "index"
        return st.session_state.get(self.global_key)
        
    def put_pages(self,pages={}):
        for i, page in enumerate(pages):
            self.put_button(page["btn_name"], i)