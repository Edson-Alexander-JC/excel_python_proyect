from abc import ABC,abstractmethod
import streamlit as st

class InputItem:
    def __init__(self,kind:str,label:str,key,unit:str,values):
        self.kind:str = kind
        self.label:str = label
        self.key = None = key
        self.unit:str = unit
        self.values = values
        
class input_llenado:
    def __init__(self,list:{str,}):
        self.list:dict = list
    def add(item:InputItem)->None:pass
    def remove(key:str)->None:pass

class RenderInterface:
    @abstractmethod
    def render()->None:pass
    
    
    
    
    #inputs_llenado
    def input_normal(item:InputItem)->None:pass
    def input_calculate(item:InputItem,label2:str,descript:str)->None:pass
    def input_normal_apreciacion(item:InputItem,apreciacion:str)->None:pass
    
    #input_list
    def input_list_create(key,n_filas,n_columnas)->None:pass
    def input_list_add(item:InputItem)->None:pass
    def input_list_remove(key)->None:pass
    
    def set_input(self,item:InputItem):
        col1, col2 = st.columns([4,1])

        with col1:
            match tipo:
                case "string": resultado = st.text_input(item.label,value=item.value or "",key=item.key)
                case "number": resultado = st.number_input(item.label,min_value=0,step=1,value=value or 0,key=key)
                case "float": resultado = st.number_input(item.label,value=value or 0.0,format="%.2f",key=key)
                case "select":
                    index = 0
                    if option in item.values: index = options.index(value)

                    resultado = st.selectbox(item.label,options,index=index,key=key)

                case "list":
                    resultado = self.input_list(item.label, key)
                case "bool":
                    resultado = st.checkbox(item.label,value=value if value is not None else False,key=key)
                case _:
                    st.warning("Tipo no soportado: " + tipo)
                    resultado = None
        with col2:
            st.markdown(f"""
                <div style="
                    display:flex;
                    align-items:end;
                    height:68px;
                    font-size:14px;
                    color:gray;
                ">{unidad}</div>
                """,
                unsafe_allow_html=True
            )

        return resultado


    def set_output(self, tipo: str, label: str, value, unidad: str = ""):
        match tipo:

            case "number":
                return st.metric(label, f"{int(value or 0)} {unidad}")

            case "float":
                return st.metric(label, f"{(value or 0):.2f} {unidad}")

            case "string":
                return st.metric(label, f"{value or ''} {unidad}")

            case "bool":
                return st.metric(label, "Sí" if value else "No")

            case _:
                st.warning("Tipo no soportado: " + tipo)
    def set_data(data):pass