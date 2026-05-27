from components.every_put import EveryPut
from interfaces.fabric_interface import FabricInterface
from data.input_item import InputItem
from domain.voladura_domain import VoladuraDomain
import streamlit as st

from data.macizo_rocoso import MacizoRocoso
from data.frente_voladura import FrenteVoladura
from data.volquete import Volquete
from data.explosivo import Explosivo
from data.maq_voladura import MaqVoladura

class VoladuraFabric(FabricInterface):
    
    
    def __init__(self):
        self.output_values = {}
        self.vd = None
        self.set_vars()
        self.render()
    def input(self,kind,key,label="",unit="",value=None,values=None):
        return self.eput.def_inputs(
            InputItem(
                kind=kind,
                key=key,
                label=label,
                value=value,
                unit=unit,
                values=values
            ))
            
                
    def output(self,key,label="",unit="",value=None):
        self.output_values[key] = value
        return self.eput.print_output(
            InputItem(
                key=key,
                label=label,
                value=value,
                unit=unit
            ))
            
    def set_vars(self):
        self.eput = EveryPut()
        
        self.frente = FrenteVoladura()
        self.roca = MacizoRocoso()
        self.volquete = Volquete()
        self.explosivo = Explosivo()
        self.maq_voladura = MaqVoladura()
    
    def def_macizo_rocoso(self):
        self.roca.name = self.input(
            key="roca_name",kind="string",
            label="Roca esteril",
            value="Roca esteril - PlaceHolder"
        )
        self.roca.pe = self.input(
            key="pe_roca",kind="float",
            label="Peso especifico de la  roca",
            value= 2.8, unit="t/m³"
        )
        self.roca.ucs = self.input(
            key="ucs",kind="float",
            label="Resistencia a la compresion simple",
            value= 200.0, unit="MPa"
        )
        self.roca.f_k_roca = self.input(
            key="f_k_roca",kind="select",
            label="Factor de la calidad de la roca",
            values=[0.7,0.8,1]
        )
        self.roca.f_esponjamiento = self.input(
            key="f_esponjamiento",kind="float",
            label="Factor de esponjamiento",
            value= 1.78, unit="%"
        )
        
    def header(self):pass

    def def_maquinaria(self):
        self.maq_voladura.name = self.input(
            key="name_maquinaria",kind="string",
            label="Que maquinaria se esta usando",
            value="Maquinaria - PlaceHolder"
        )
        self.maq_voladura.diametro_broca = self.input(
            key="diametro_broca",kind="float",
            label="Diametro de la broca",
            unit="mm", value=45.0
        )
        self.maq_voladura.long_barra = self.input(
            key="long_barra",kind="float",
            label="Largo de la barra",
            unit="m", value= 4.27
        )        
        
    def def_frente_voladura(self):
        self.frente.kind = self.input(
                key="b",kind="radio",
                label="Tipo de frente de voladura",
                values=["M.Superficial","M.Subterranea"]
        )
        self.frente.b = self.input(
                key="b",kind="float",
                label="ancho del frente de voladura",
                unit="m", value=35.0
        )
        self.frente.h = self.input(
                key="h",kind="float",
                label="largo del frente de voladura",
                unit="m", value=15.0
        )
        self.frente.z = self.input(
                key="z",kind="float",
                label="espesor del frente de voladura",
                unit="m", value=4.0
        )
        self.frente.espaciamiento = self.input(
                key="espacimiento",kind="float",
                label="espacimiento del frente de voladura",
                unit="m", value=1.4
        )
        self.frente.burden = self.input(
                key="burden",kind="float",
                label="burden del frente de voladura",
                unit="m", value=4.0
        )
       
    def def_explosivo(self):
        self.explosivo.name = self.input(
                key="exp_name",kind="string",
                label="Que explosivo se esta usando",
                value="Explosivo - PlaceHolder"
        )
        self.explosivo.diametro_explosivo = self.input(
                key="diametro_exp",kind="float",
                label="Diametro del explosivo",
                unit="mm", value=32.0
        )
        self.explosivo.long_explosivo = self.input(
                key="long_explosivo",kind="float",
                label="Factor de arranque del explosivo",
                unit="cm", value=20.0
        )
        self.explosivo.vod = self.input(
                key="vod",kind="float",
                label="Velocidad de detonacion",
                unit="m/s", value=4000.0
        )
        self.explosivo.pe = self.input(
                key="pe_exp",kind="float",
                label="Densidad del explosivo",
                unit="g/cm³", value=0.80
        )
        self.explosivo.f_arranque = self.input(
                key="f_arranque",kind="float",
                label="Factor de arranque del explosivo",
                unit="%", value=0.85
        )
        self.explosivo.f_potencia = self.input(
                key="f_potencia",kind="float",
                label="Factor de arranque del explosivo",
                unit="kg/ton", value=0.4
        )
        self.explosivo.calor = self.input(
                key="calor",kind="float",
                label="Factor de arranque del explosivo",
                unit="kcal/kg", value=912.0
        )
    
    def def_volquetes(self):
        self.volquete.name = self.input(
                key="volquete_name",kind="string",
                label="Que volquete se esta usando",
                value="Volquete - PlaceHolder"
        )
        self.volquete.cap = self.input(
                key="cap_volquete",kind="float",
                label="Capacidad del volquete",
                unit="m³",value=22.0
        )
        self.volquete.renta = self.input(
                key="renta_volquete",kind="float",
                label="Precio de renta por hora",
                unit="soles", value=180.0
        )
    
    def def_combustible(self):
        self.gasol_maq_voladura : float = self.input(
                key="renta_gasol_maq_voladura",
                kind="float",
                label="Consumo de la maquina de voladura",
                unit="gal/h"
        )
        self.gasol_volquete : float = self.input(
                key="gasol_volquete",
                kind="float",
                label="Consumo del volquete",
                unit="gal/h"
        )
        
    def set_view_to_put(self):
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.subheader("Macizo Rocoso")
            self.def_macizo_rocoso()
        with c2:
            st.subheader("Frente de Voladura")
            self.def_frente_voladura()
        with c3:
            st.subheader("Maquinaria")
            self.def_maquinaria()
        with c4:
            st.subheader("Explosivo")
            self.def_explosivo()
        
        st.divider()
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.subheader("Volquetes")
            self.def_volquetes()
        with c2:
            st.subheader("Combustible")
            self.def_combustible()
        
        st.divider()
        self.calular = st.button("Calcular",width="stretch")
        
    def set_view_to_output(self):
        if(self.vd != None): return
        
        self.vd = VoladuraDomain(
            frente = self.frente,
            roca = self.roca,
            volquete = self.volquete,
            explosivo = self.explosivo,
            maq_voladura = self.maq_voladura,
        )
        self.set_output_view()
        
        
        
        
    def set_column(self,dim):
        return st.columns(dim)
    def put_column(self,poss,columnas,elemento):
        with columnas[poss]:
            elemento()
    def mk_col(self,elements:list):
        colmuna = self.set_column(len(elements))
        
        for i, element in enumerate(elements):
            self.put_column(i,colmuna,element)
        
    
    def set_ton_vol(self):
        st.subheader("Tonelaje y Volumen")
        self.mk_col([
            lambda: self.output(
                key="volumen_real",
                label="Volumen real",
                unit="m³",
                value=self.vd.volumen_real()
            ),

            lambda: self.output(
                key="tonelaje",
                label="Tonelaje",
                unit="t",
                value=self.vd.tonelaje()
            ),
        ])
        
    def set_burdenes(self):
        st.subheader("Burdenes y nro Taladros")
        
        self.output(
            key="burden_escogido",unit="m",
            label="burden, que nosotros hemos colocamos",
            value= self.frente.burden,
        )
        
        self.mk_col([
            lambda: self.output(
                key="burden_pearse_1955",unit="m",
                label="burden, segun pearse (1955)",
                value= self.vd.burden_pearse_1955(),
            ),
            lambda: self.output(
                key="burden_andersen_1952",unit="m",
                label="burden, segun andersen (1952)",
                value= self.vd.burden_andersen_1952(),
            ),
            lambda: self.output(
                key="burden_fraenkel_1952",unit="m",
                label="burden, segun fraenkel (1952)",
                value= self.vd.burden_fraenkel_1952(),
            )
        ])
        self.mk_col([
            lambda: {
                    self.output(
                        key="burden_konya_1976",unit="m",
                        label="burden, segun konya (1976)",
                        value= self.vd.burden_konya_1976(),
                    ),
                    self.output(
                        key="espaciamiento_konya_1976",unit="m",
                        label="espaciamiento, segun konya (1976)",
                        value= self.vd.espaciamiento_Konya_1976(),
                    ),
                    self.output(
                        key="taco_konya_1976",unit="m",
                        label="taco, segun konya (1976)",
                        value= self.vd.taco_Konya_1976(),
                    )
                },
            lambda: {
                    self.output(
                        key="f_energia_JKRMC_1986",unit="Kcal/t ",
                        label="factor de energia, segun Lily (1986)",
                        value= self.vd.f_energia_JKRMC_1986(),
                    ),
                    self.output(
                        key="f_carga_JKRMC_1986",unit="g/t",
                        label="factor de carga, segun Lily (1986)",
                        value= self.vd.f_carga_JKRMC_1986(),
                    ),
                    self.output(
                        key="burden_JKRMC_1986",unit="m",
                        label="burden, segun Lily (1986)",
                        value= self.vd.burden_JKRMC_1986(),
                    ),
                }
        ])
        
        self.output(
            label="burden promedio", key="burden_prom",
            unit="m", value= self.vd.promedio_burden()
        )
        
        
    def set_output_view(self):
        self.set_ton_vol()
        st.divider()
        self.set_burdenes()
        self.mk_col([
            lambda: self.output(
                key="volumen_real",label="Volumen real",
                unit="m³",value=self.vd.volumen_real()
            ),

            lambda: self.output(
                key="tonelaje",label="Tonelaje",
                unit="t",value=self.vd.tonelaje()
            ),
        ])
        
    def view_arquitecture(self):
        tab1, tab2, tab3 = st.tabs([
            "Ingresar los datos",
            "Datos calculados",
            "Configuración"
        ])

        with tab1:
            self.set_view_to_put()
        with tab2:
            st.subheader("Calculos")
            if(self.calular) : self.set_view_to_output()
            
        with tab3:
            st.write("Configuración")
            
    def render(self):
        self.view_arquitecture()
        
        
    