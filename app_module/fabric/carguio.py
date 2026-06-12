import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.interfaces.input_item import InputItem

class Carguio(FabricInterface):
    def render_sidebar(self):pass
    def set_vars(self):pass

    def render_view(self):
        st.title("Propiedades del Explosivo")
        self.make_arquitecture()

    def make_arquitecture(self):
        vel_penetracion = self.ep.print_input(InputItem(
            key="vel_penetracion", kind="number",
            label="Velocidad de penetracion", 
        ))
        nro_brazos = self.ep.print_input(InputItem(
            key="nro_brazos", kind="number",
            label="Numero de brazos de la maquina", 
        ))
        t_posicionamiento = self.ep.print_input(InputItem(
            key="t_posicionamiento", kind="number", 
            label="Tiempo que tarda el brazo de un punto a otro", 
        ))
        t_traslado = self.ep.print_input(InputItem(
            key="t_traslado", kind="number", 
            label="Tiempo del traslado del personal", 
        ))

    def render(self):
        self.render_sidebar()
        self.render_view()
