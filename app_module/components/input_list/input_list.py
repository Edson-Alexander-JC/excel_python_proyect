import copy
import streamlit as st
from dataclasses import asdict, is_dataclass
from pathlib import Path
from app_module.interfaces.input_item import InputItem

input_list_js = Path("app_module/components/input_list/input_list.js").read_text("utf-8")

class InputList():
    def __init__(self,data:InputItem):
        domain_js = Path("app_module/components/input_list/modules/domain.js").read_text("utf-8")
        structure_js = Path("app_module/components/input_list/modules/structure.js").read_text("utf-8")
        html=Path("app_module/components/input_list/input_list.html").read_text(encoding="utf-8")
        css=Path("app_module/components/input_list/input_list.css").read_text(encoding="utf-8")
        
        self.raw_data = data
        self.data = asdict(data) if is_dataclass(data) else data
        
        self.component_plantilla = st.components.v2.component(
            name="input_list",
            html=html,
            css=css,
            js=domain_js + "\n" + structure_js + "\n" + input_list_js
        )

    def render(self):
        data_prepared = self.prepare_data()
        self.component_render = self.component_plantilla(
            key=self.data["key"],
            data=data_prepared,
            on_new_change = lambda: None
        )
        
        if not self.component_render: return []
        return self
    
    def get_values(self):
        if not hasattr(self, "component_render"): return []
        if not hasattr(self.component_render, "items_list"): return []
        return self.component_render.items_list
    
    def filtrar_data(self,columna):
        items = self.get_values()
        filtrado = {}
        
        for item in items:
            for i, value in enumerate(item.get("values", [])):
                if value["columna"] == columna:
                    try:
                        numeric_value = float(value["value"])
                        filtrado[i] = numeric_value
                    except (ValueError, TypeError):
                        pass
                    break
                
        return filtrado
    
    def sumatoria_filtrado(self,columna):
        filtrado = self.filtrar_data(columna)
        
        if "values" not in filtrado: return 0
        return sum(filtrado["values"])
    
    def promedio_filtrado(self,columna):
        filtrado = self.filtrar_data(columna)
        
        if len(filtrado) == 0: return 1
        return self.sumatoria_filtrado(columna) / len(filtrado)
    
    def get_columns(self,data,col):
        columnas = []
        inputs = data["value"]["values"]
        for input in inputs:
            columnas.append(input[col])
        return columnas
    
    def put_columns(self,data):
        if(not data["values"]): return
        
        columnas = self.get_columns(data,"key")
        units = self.get_columns(data,"unit")
        
        for out_puts in data["values"]:
            for x in range(len(out_puts["values"])):
                out_puts["values"][x]["key"] = columnas[x]
                out_puts["values"][x]["unit"] = units[x]
                
    def prepare_data(self):
        data = copy.deepcopy(self.data)
        self.put_columns(data)
        return data
        
    def sumatoria_all(self):
        data = self.get_values()
        sumar_list = {}

        for out_puts in data:
            for output in out_puts["values"]:
                value = output["value"]

                try:
                    numeric_value = float(value)
                    col = output["columna"]
                    
                    if col not in sumar_list:
                        sumar_list[col] = 0
                        
                    sumar_list[col] += numeric_value
                except (ValueError, TypeError):
                    pass
        return sumar_list
    
    def promedio_all(self):
        data = self.get_values()
        sumar_list = {}

        for out_puts in data:
            for output in out_puts.get("values", []):
                value = output.get("value")

                if isinstance(value, (int, float)):
                    col = output.get("columna")

                    if col not in sumar_list:
                        sumar_list[col] = 0

                    sumar_list[col] += value

        return sumar_list

