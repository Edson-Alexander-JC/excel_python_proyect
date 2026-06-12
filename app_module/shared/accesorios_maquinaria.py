import streamlit as st
from app_module.interfaces.input_item import InputItem
from app_module.shared.every_put import EveryPut
from app_module.shared.colum_setter import ColumnSetter
from app_module.shared.data_full_verify import DataFullVerify

class AccesoriosMaquinaria():
    def __init__(self):
        self.ep : EveryPut = EveryPut()
        self.cs : ColumnSetter = ColumnSetter()
        self.dfv : DataFullVerify = DataFullVerify()
            
    def set_maquinaria(self,maq_name):
        self.maq_name = maq_name
        self.my_key = self.maq_name+"_accesorios_list"
        
        if self.my_key not in st.session_state:
            st.session_state[self.my_key] = []
    
    def render_accesorios(self,items=[]):
        self.my_accesorios = self.ep.print_input(InputItem(
            kind="list",key=self.my_key,
            label="Accesorios y su Cantidad: ",
            value=InputItem(values=[
                InputItem(
                    label="Nombre del Accesorio: ",kind="string",
                    key=("accesorio_"+self.maq_name)
                ),
                InputItem(
                    label="Cantidad: ", key=("cant_"+self.maq_name),
                    kind="number"
                ),
            ]),
            values=items
            )
        )
        self.expanders()

    def print_expanders(self,expander_list):
        for expander in expander_list:
            expander()
            
    def set_expander(self,label,key,cant):
        
        st.html(f"""<style>
            .st-key-{key} {{
                min-width:500px;
            }}
        </style>""")
        with st.expander(label,key=key):
            
            
            self.cs.mk_col([
                lambda:self.ep.print_output(InputItem(
                    key=key+"_cant", label="cantidad",
                    kind="number", value=cant
                ),padding=True,h_aling="center",v_aling="center"),
                lambda:self.ep.print_input(InputItem(
                    key=key+"_presentacion",
                    label="Presentacion", kind="select",
                    values=[
                        #EMBASES
                        "Bolsa","Paquete","Caja","Rollo",
                        #UNIDADES FISICA
                        "l","ml","kg","g","m","cm"
                        #UNIDAD
                        "unidad"
                    ]
                ))
            ])   
            
            self.cs.mk_col([
                lambda: self.ep.print_input(InputItem(
                    key=key+"_vu", label="Vida Util: ", 
                    kind="string",
                )),
                lambda: self.ep.print_input(InputItem(
                        key=key+"_unit_vu", label="Unidad: ", 
                        kind="select", 
                        values=[
                            #DISTANCIA
                            "m","inch","ft","mm","cm",
                            #TIEMPO
                            "año","semana","dia"
                            #USO
                            ,"uso/ciclo"
                        ]
                ))
            ])
            
            costo_unit = st.session_state.get(key+"_cost_unit",0)
            
            self.cs.mk_col([
                lambda: self.ep.print_input(InputItem(
                        key=key+"_cost_unit",
                        label="Costo c/u", kind="number",
                        unit="$/"+str(st.session_state[key+"_presentacion"]),
                )),
                lambda: self.ep.print_output(InputItem(
                    key=key+"_total_cost", label="Costo Total",
                    kind="number", value=(costo_unit*cant), unit="soles"
                ),  padding=True,h_aling="center",v_aling="center")
            ])
            
    
          
    def expanders(self):
        accesorios = self.my_accesorios.get_values()
        expander_list = []
        
        for accesorio in accesorios:
            key = accesorio["item_key"]
            label_expander = accesorio["values"][0]["value"]
            cant = accesorio["values"][1]["value"]
            
            expander_list.append(
                lambda k=key, lbl=label_expander, c=cant:
                    self.set_expander(lbl, k, c)
            )
        
        key_expander_container = self.my_key+"_expander_container"
        st.html(
            f"""
            <style>
                .st-key-{key_expander_container} {{
                    display:flex;
                    overflow-x:auto;
                    flex-direction: row;
                    gap: 10px;
                    width:full;
                    padding: 10px 20px;
                }}
            </style>
            """
        )
        
        with st.container(key=key_expander_container):
            self.print_expanders(expander_list)


    