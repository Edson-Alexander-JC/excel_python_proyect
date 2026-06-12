import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface
class GeomecanicaFabric(FabricInterface):
    def set_vars(self):pass
    def render_sidebar(self):pass
    def render_view(self):pass
    def make_arquitecture(self):pass
    
    def ready(self):
        self.set_vars()
    
    def render(self): self.make_arquitecture()
    
    pass