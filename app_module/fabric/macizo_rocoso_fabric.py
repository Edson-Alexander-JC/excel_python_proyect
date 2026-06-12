import streamlit as st
from app_module.interfaces.fabric_interface import FabricInterface
from app_module.interfaces.input_item import InputItem
from app_module.shared.demoras_global import DemorasGlobal

class PerforadoraFabric(FabricInterface):
    def set_vars(self):pass
    def render_sidebar(self):pass
    
        
    
    def demoras_operacionales_list(self):
        demoras_perforadora = self.ep.print_input(InputItem(
            kind="list",key="dop",
            label="Demoras operativas de la perforadora (min/turno)",
            value=InputItem(values=[
                InputItem(
                    label="concepto de la demora",
                    key="concepto_dop",kind="string"
                ),
                InputItem(
                    label="tiempo",
                    key="demoras_dop",kind="number",unit="min"
                )
            ]),
            
            values=[
                InputItem(key="fuel_gas",values=[
                    InputItem(value="Abastecimiento del combustible"),
                    InputItem(value=40),
                ]),
                *DemorasGlobal.get_demoras(),
            ])
        )
    
    def demoras_ciclo_list(self):
        demoras_ciclo_list = self.ep.print_input(InputItem(
            kind="list",key="dcp",
            label="Demoras operativas de la perforadora (min/turno)",
            value=InputItem(values=[
                InputItem(
                    label="concepto de la demora",
                    key="concepto_dcp",kind="string"
                ),
                InputItem(
                    label="tiempo",
                    key="demoras_dcp",kind="number",unit="min"
                ),
            ]),
            
            values=[
                InputItem(key="change_barras",values=[
                    InputItem(value="Cambio/Adicion de barra"),
                    InputItem(value=30),
                ]),
                InputItem(key="pos_niv",values=[
                    InputItem(value="Posicionamientos y nivelacion"),
                    InputItem(value=35),
                ]),
                InputItem(key="change_brocas",values=[
                    InputItem(value="Cambio de brocas"),
                    InputItem(value=30),
                ]),
                InputItem(key="clean_pozo",values=[
                    InputItem(value="Limpieza/Soplado del pozo"),
                    InputItem(value=20),
                ]),
            ])
        )
    
    def demoras(self):
        self.cs.mk_col({
            lambda:self.demoras_operacionales_list(),
            lambda:self.demoras_ciclo_list()
        })
    
    def accesorios(self):
        st.divider()
        st.subheader("Accesorios")
        
        if(st.session_state["mine_type"] == "Subterranea"):
            st.session_state["largo_barra"] = 8
        else:        
            st.session_state["largo_barra"] = 15
        
        self.cs.mk_col({
            lambda: self.ep.print_input(InputItem(
                key="largo_barra", 
                kind="number", unit="m",
                label="Largo de una barra"
            )),
            lambda: self.ep.print_input(InputItem(
                key="nro_brazos", kind="number",
                label="Numero de brazos de la maquina", 
                value=1
            )),
            lambda: self.ep.print_input(InputItem(
                key="diametro_broca", 
                kind="number", value=5, unit="pulg",
                label="Diametro de la broca"
            )),
        })
        
    def horas(self):
        self.cs.mk_col({
            lambda: self.ep.print_input(InputItem(
                key="h_turno_perforacion", 
                kind="number", value=12,unit="h/turno",
                label="horas por cada turno"
                
            )),
            lambda: self.ep.print_input(InputItem(
                key="h_mantenimiento_c_perforadora", 
                kind="float", value=1.5,unit="h/turno",
                label="mantenimiento correctivo"
                
            )),
            lambda: self.ep.print_input(InputItem(
                key="h_mantenimiento_p_perforadora", 
                kind="float", value=1.5,unit="h/turno",
                label="mantenimiento preventivo"
                
            ))
        })
        
    def render_view(self):
        st.subheader("Tiempos")
        
        self.horas()
        self.demoras()
        self.accesorios()
        
        
        
        
        
        
    def make_arquitecture(self):self.render_view()
    