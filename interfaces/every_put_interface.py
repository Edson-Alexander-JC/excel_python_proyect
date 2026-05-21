import streamlit as st
from data.input_item import InputItem
from interfaces.input_llenado import InputLlenado

class EveryPutInterface:
    def __init__(self):
        pass
    #inputs_llenado
    def input_normal(self,item:InputItem)->None: 
        self.set_input(item)
    def input_calculate(item:InputItem,label2:str,descript:str)->None:pass
    def input_normal_apreciacion(item:InputItem,apreciacion:str)->None:pass
    #input_list
    def input_list_create(key,n_filas,n_columnas)->None:pass
    def input_list_add(item:InputItem)->None:pass
    def input_list_remove(key)->None:pass
    
    def input_list(self,item:InputItem,border:bool=True):
        subinputs : InputItem = item.value
        inputs = subinputs.values
        
        target_col = self.ajustar_componente(inputs)
        ancho = self.calc_filas(inputs)
        
        with target_col:
            with st.container(border=border,vertical_alignment="center"):
                columnas = st.columns(ancho, gap="small",vertical_alignment="center")
                values = self.print_filas(inputs, columnas)
                
        #Estado de seleccion
        selector_event = f"{item.key}_item_index"
        if selector_event not in st.session_state:
            st.session_state[selector_event] = None

        return values
        
    def print_filas(self, elements: list[InputItem], columnas):
        values = []
        for i, element in enumerate(elements):
            with columnas[i]:
                value = self.render_input(element)
                values.append(value)

        return values
    
    def calc_filas(self,elements: list[InputItem]):
        
        widths = [
            getattr(element, "width", 1)
            for element in elements
        ]
        
        return widths
    
    def ajustar_componente(
        self,
        elements: list[InputItem],
        alignment: str = "center",
        border: bool = True,
        margin_left: float = 1.0,
        margin_right: float = 1.0,
    ):
        
        # Suma total del ancho
        total_width = sum(self.calc_filas(elements))
        values = []
        outer_cols = []
        match alignment:
            case "left":
                outer_cols = st.columns([total_width, 1 * margin_right], 
                                        gap="small",vertical_alignment="center")
                target_col = outer_cols[0]
            case "center":
                outer_cols = st.columns([1 * margin_left, total_width, 1 * margin_right], 
                                        gap="small",vertical_alignment="center")
                target_col = outer_cols[1]
            case "right":
                outer_cols = st.columns([1 * margin_left, total_width],
                                        gap="small",vertical_alignment="center")
                target_col = outer_cols[1]
        
        return target_col
    
    def get_label(self, item):
        if item.label and item.label.strip():
            return item.label, "visible"
        return "label", "collapsed"
    
    def get_unit(self,item:InputItem):
        if item.unit:
            st.markdown(
                f"""
                <div style="
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    min-height:38px;
                    font-size:14px;
                    color:#666;
                ">
                    {item.unit}
                </div>
                """,
                unsafe_allow_html=True,
            )

    
    def set_input(self,item:InputItem):
        label, visibility = self.get_label(item)
        
        match item.kind:
            case "string": 
                resultado = st.text_input(
                    label,label_visibility=visibility,
                    value=item.value or "",
                    key=item.key
                )
            case "number": 
                resultado = st.number_input(
                    label,label_visibility=visibility,
                    min_value=0,step=1,
                    value=item.value or 0,
                    key=item.key
                )
            case "float": 
                resultado = st.number_input(
                    label,label_visibility=visibility,
                    min_value=0.0,
                    value=item.value or 0.0,format="%.2f",
                    key=item.key
                )
            case "select":
                str_list = [str(x) for x in item.values]
                resultado = st.selectbox(
                    label,
                    str_list,
                    label_visibility=visibility,
                    index=0,
                    key=item.key
                )
            case "list":
                resultado = self.input_list(item)
                    
            case "bool":
                resultado = st.checkbox(
                    label,label_visibility=visibility,
                    value=item.value if item.value is not None else False,
                    key=item.key
                )

            case _:
                st.warning("Tipo no soportado: " + item.kind)
                resultado = None

        return resultado


    def set_output(self,item:InputItem):
        label, visibility = self.get_label(item)
        match item.kind:

            case "number":
                return st.metric(
                    label,
                    f"{int(item.value or 0)} {item.unit}",
                    label_visibility=visibility,
                )

            case "float":
                return st.metric(
                    label, 
                    f"{(item.value or 0):.2f} {item.unit}",
                    label_visibility=visibility,
                )

            case "string":
                return st.metric(
                    label, 
                    f"{item.value or ''} {item.unit}",
                    label_visibility=visibility,
                )

            case "select":
                return st.metric(
                    label,
                    f"{item.value[0] or ''} {item.unit}",
                    label_visibility=visibility,
                )

            case "bool":
                return st.metric(
                    label, 
                    "Sí" if item.value else "No",
                    label_visibility=visibility,
                )

            case "list":
                items_default : InputItem = item.values
                for i,sub_item in enumerate(items_default):
                    componentes = sub_item.values
                    cols = st.columns(len(componentes))
                    for i,sub_componente in enumerate(componentes):
                        with cols[i]:
                            self.set_output(sub_componente)
            case _:
                st.warning("Tipo no soportado: " + item.kind)
    def set_data(data):pass
    def render_buttons(self,item:InputItem):
        buttons = [
            ("+",    f"{item.key}_add",    lambda: self.input_list_add(item)),
            ("-",    f"{item.key}_remove", lambda: self.input_list_remove(item.key)),
            ("Rest", f"{item.key}_create", lambda: self.input_list_create(item.key)),
        ]
        for col, (label, key, action) in zip(st.columns(3,width="stretch",gap="small"), buttons):
            with col:
                if st.button(label, key=key):
                    action()   # Aquí se ejecuta la función asociada
    def get_additionals(self,item:InputItem):
        renderers = []
        
        unit = getattr(item, "unit", None)
        if unit and unit != "":
            renderers.append(lambda: self.get_unit(item))
        
        if item.kind == "list":
            renderers.append(lambda: self.render_buttons(item))
                
        return renderers
    
    def render_addtionals(self,item:InputItem):
        additionals = self.get_additionals(item)
        cols = st.columns(len(additionals), gap="small",width="stretch")

        # Renderiza cada adicional en su propia columna
        for col, render in zip(cols, additionals):
            with col:
                render()
        
    def render_input(self, item: InputItem):
        # ---------------------------------------------------------
        # CONFIGURACIÓN BASE
        # ---------------------------------------------------------
        TOTAL = 12  # Total de unidades de ancho (tipo Bootstrap)

        # Pesos fijos
        INPUT_WEIGHT = 10
        UNIT_WEIGHT = 1
        BUTTONS_WEIGHT = 1

        # ---------------------------------------------------------
        # CONSTRUIR ESPECIFICACIÓN
        # ---------------------------------------------------------
        spec = []
        renderers = []

        # Input principal
        spec.append(INPUT_WEIGHT)
        renderers.append(lambda: self.set_input(item))

        # Unidad
        if item.unit:
            spec.append(UNIT_WEIGHT)
            renderers.append(lambda: self.get_unit(item))

        # Botones
        if item.kind == "list":
            spec.append(BUTTONS_WEIGHT)
            renderers.append(lambda: self.render_buttons(item))

        # ---------------------------------------------------------
        # CALCULAR MÁRGENES AUTOMÁTICOS
        # ---------------------------------------------------------
        used = sum(spec)

        # Si used > TOTAL, expandir TOTAL para evitar valores negativos
        total_width = max(TOTAL, used)

        free_space = total_width - used

        # Repartir el espacio libre a ambos lados
        left_margin = free_space // 2
        right_margin = free_space - left_margin

        # Solo agregar márgenes si son mayores a 0
        final_spec = []

        if left_margin > 0:
            final_spec.append(left_margin)

        final_spec.extend(spec)

        if right_margin > 0:
            final_spec.append(right_margin)

        # ---------------------------------------------------------
        # CREAR COLUMNAS
        # ---------------------------------------------------------
        cols = st.columns(
            final_spec,
            gap="small",
            vertical_alignment="center",
        )

        # Índice inicial (saltando margen izquierdo si existe)
        start = 1 if left_margin > 0 else 0

        resultado = None

        # ---------------------------------------------------------
        # RENDERIZAR ELEMENTOS
        # ---------------------------------------------------------
        for i, render in enumerate(renderers):
            with cols[start + i]:
                value = render()

                # El primer renderer corresponde al input principal
                if i == 0:
                    resultado = value

        return resultado