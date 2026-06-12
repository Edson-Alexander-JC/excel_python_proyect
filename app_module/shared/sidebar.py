import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface

class SideBar():
    def def_pages(self,list:{str,FabricInterface}):
        self.pages = list

    def render_sidebar(self, msg:str=""): 
        with st.sidebar:
            self.selected = st.sidebar.selectbox(
                msg,self.pages.keys()
            )
            
            if hasattr(self.pages[self.selected],"render_sidebar"):
                self.pages[self.selected].render_sidebar()
        
    def render_view(self):
        if hasattr(self.pages[self.selected],"render_view"):
            self.pages[self.selected].render_view()

    
        