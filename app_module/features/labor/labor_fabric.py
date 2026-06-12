import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.interfaces.input_item import InputItem
from app_module.shared.demoras_part import DemorasPart
from app_module.shared.button_sidebar_element import ButtonSidebarElement
from app_module.fabric.geomecanica_fabric import GeomecanicaFabric

class LaborFabric(FabricInterface):
    def set_vars(self):
        self.dp = DemorasPart(
            "dp_list",
            "demoras programadas adicionales"
        )
        
    def render_sidebar(self):pass
            
    def turnos(self):
        
        self.cs.mk_col([
            lambda:self.ep.print_input(InputItem(
                key="nro_turnos", kind="number",
                label="Nro turnos: ", value=2, 
                unit="turnos"
            )),
            lambda:self.horas_turno()
        ])
        
    def horas_turno(self):
        nro = st.session_state.nro_turnos
        
        if "ultimo_nro" not in st.session_state:
            st.session_state.ultimo_nro = nro

        if "h_turno" not in st.session_state:
            st.session_state.h_turno = round(24 / nro)

        # Solo recalcular cuando cambia nro_turnos
        if nro != st.session_state.ultimo_nro:
            st.session_state.h_turno = round(24 / nro)
            st.session_state.ultimo_nro = nro
            
        self.ep.print_input(InputItem(
            key="h_turno", kind="number",
            label="Horas por turno: ",
            unit="h"
        ))
        
    def render_view(self):
        st.header("Propiedades de la Labor")
        self.turnos()
        
        self.cs.mk_col([
            lambda: self.ep.print_input(InputItem(
                key="t_refrigerio", kind="number",
                label="Refrigerio: ", value=45,
                unit="min"
            )),
            lambda:self.ep.print_input(InputItem(
                key="t_traslado", kind="number",
                label="Traslado: ", value=45,
                unit="min"
            )),
            lambda: self.ep.print_input(InputItem(
                key="t_charla", kind="number",
                label="Charla de seguridad", value=20,
                unit="min"
            )),
        
            lambda: self.ep.print_input(InputItem(
                key="t_turnos", kind="number",
                label="Cambio de turno: ", value=15,
                unit="min"
            ))
        ])
        
        label_demoras = "Otras Demoras Programadas adicionales"
        
        self.cs.mk_col([
            lambda:self.dp.make_demoras(label_demoras),
            lambda:self.calc_demoras_programadas(),
        ])
        
    def calc_demoras_programadas(self):
        
        st.header("Calculos de Tiempos")
        
        t_refrigerio = st.session_state["t_refrigerio"]
        t_traslado = st.session_state["t_traslado"]
        t_charla = st.session_state["t_charla"]
        t_turnos = st.session_state["t_turnos"]
        t_dp_list = self.dp.get_sumatoria()
        
        horas_x_turno = st.session_state.get("h_turno")
        
        self.ep.print_output(InputItem(
            key="dp_total", kind="number",
            label="Tiempo Disponible: ", value=horas_x_turno,
            unit="h"
        ))
        
        sumatoria = sum([
            t_refrigerio,
            t_traslado,
            t_charla,
            t_turnos,
            t_dp_list,
        ])
        
        demoras_programadas = round(sumatoria/60)
        
        self.ep.print_output(InputItem(
            key="dp_total", kind="number",
            label="Demoras programadas: ", value=demoras_programadas,
            unit="h"
        ))
        
        horas_programadas = horas_x_turno - demoras_programadas
        
        self.ep.print_output(InputItem(
            key="dp_total", kind="number",
            label="Tiempo Operativo: ", value=horas_programadas,
            unit="h"
        ))
        
        
        
    def make_arquitecture(self):pass
        
    