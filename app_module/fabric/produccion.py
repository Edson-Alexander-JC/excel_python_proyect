import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.interfaces.input_item import InputItem
class Produccion(FabricInterface):
    def render_sidebar(self):pass
    def set_vars(self):pass

    def render_view(self):
        st.title("Propiedades de la operacion")
        self.make_arquitecture()

    def make_arquitecture(self):
        
        self.tiempos_part()
        st.divider()
        self.results()
            
    def set_time_col(self):
        self.d_operacion = self.ep.print_input(InputItem(
            key="d_operacion", kind="number",
            label="Dias de Operacion al Año", 
            unit="dias", value=360
        ))
        self.nro_turnos = self.ep.print_input(InputItem(
                key="nro_turnos", kind="number",
                label="turnos al dia", value=2,
                unit="turnos"
        ))
        self.h_turno = self.ep.print_input(InputItem(
                key="h_turno", kind="number",
                label="Horas por turno", unit="h",
                value=11
        ))
        self.prod_anual = self.ep.print_input(InputItem(
            key="prod_anual", kind="number",
            label="Produccion Anual", unit="t/dia",
            value=2000
        ))

    def demoras_operativas(self):
        self.h_demoras = self.ep.print_input(InputItem(
            key="h_demoras", kind="list", 
            label="Demoras Operativas", 
            value=InputItem(values=[
                InputItem(
                    kind="string",key="concepto_min_demora",
                    label="Concepto"
                ),
                InputItem(
                    kind="number",key="minutos_demora",
                    label="Minutos de la demora", unit="min"
                ),
            ]),
            values=[InputItem(key="t_refrigerio",
                values=[
                    InputItem(value="Tiempo de refrigerio"),
                    InputItem(value=60),
                ]),
                InputItem(key="t_charla",
                values=[
                    InputItem(value="Charla de induccion"),
                    InputItem(value=20),
                ]),
                InputItem(key="t_traslado",
                values=[
                    InputItem(value="Traslado del personal"),
                    InputItem(value=15),
                ]),
                
                
            ]
        ))
        
    def tiempos_part(self):
        st.subheader("Tiempos labores")
        self.cs.mk_col([
            lambda: self.demoras_operativas(),
            lambda: self.set_time_col()
            ,             
        ])


    def render(self):
        self.render_sidebar()
        self.render_view()

    def results(self):
        data = [
            self.prod_anual,
            self.d_operacion,
            self.nro_turnos,
            self.h_turno,
        ]
        data = data + list(self.h_demoras.sumatoria_all().values())
        if(self.dfv.verify(data)):
            st.subheader("Calculos")
    