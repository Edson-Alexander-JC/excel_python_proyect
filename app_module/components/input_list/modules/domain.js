console.log("DOMINIO CARGADO");
window.MyApp = window.MyApp || {};
window.MyApp.componets = window.MyApp.componets || {};

if (!window.MyApp.DomainComponent) {

    window.MyApp.DomainComponent = class {

    init(component){
        const {
            parentElement,
            setStateValue,
            setTriggerValue,
            data
        } = component;

        const key = data.key;
        const my_state = window.MyApp.componets[key];
        this.my_state = my_state;
        this.data = data;
        this.setStateValue = setStateValue;
        this.setTriggerValue = setTriggerValue;

        if (my_state.states.domain) return;
        my_state.states.domain = true;
        
        //inicializacion
        console.log("------------");
        // console.log("key =", data.key);
        // console.log("data.values =", data.values);
        // console.log("state existente =", window.MyApp.state[data.key]);

        this.needs_update = false;
        this.my_state.items_list = {};
        this.my_state.columnas = data.value.values.map(item => item.key);
        this.my_state.target_item = null;
        this.my_state.items_initialized = false;
        
        console.log("state final =", this.my_state);
    }

    del_btn(){
        const target_item = this.my_state.target_item;
        if(!target_item) return;

        this.my_state.items_list = this.my_state.items_list.filter(
            item => item.etiqueta !== target_item
        );

        this.mark_dirty();
        return target_item;
    }

    put_target_item(item_key){
        this.my_state.target_item = item_key;
    }

    selects_emptys(selects){
        const hasEmptySelects = Array.from(selects).some(select => {
            return select.options[select.selectedIndex].text.trim() === "";
        });
        return hasEmptySelects;
    }
    
    inputs_emptys(inputs){
        const hasEmptyInputs = Array.from(inputs).some(input => {
            // ignorar checkbox
            if(input.type === "checkbox"){
                return false;
            }
            return input.value.trim() === "";
        });
        return hasEmptyInputs;
    }
    
    verificar_inputs(inputs, selects){
        const hasEmptyInputs = this.inputs_emptys(inputs);
        const hasEmptySelects = this.selects_emptys(selects);

        return (hasEmptyInputs || hasEmptySelects);
    }

    add_btn(inputs, selects){
        if(this.verificar_inputs(inputs, selects)) return;
        const new_row = this.agrupar_inputs(inputs, selects);
        const new_item = this.make_item(new_row);
        this.registrar_item(new_item)
        return new_item;
    }

    agrupar_inputs(inputs, selects){
        const new_row = {
            key: "custom",
            values: [
                ...Array.from(inputs).map(input => ({
                    value: input.type === "checkbox"
                        ? input.checked
                        : input.value,                    
                    key: input.dataset.key,
                    unit: input.dataset.unit || ""
                })),

                ...Array.from(selects).map(select => ({
                    value: select.options[select.selectedIndex].text,
                    key: select.dataset.key,
                    unit: select.dataset.unit || ""
                }))
            ],
            etiqueta: "",
        };
        return new_row;
    }
    
    mismos_items(values){
        return Object.values(this.my_state.items_list).some(
            item => JSON.stringify(item.values) === JSON.stringify(values)
        );
    }
    
    order_by_cols(inputs_items){
        const result = [];
        this.my_state.columnas.forEach(col => {
            inputs_items.values.forEach(value => {
                if(value["key"]===col){
                    result.push(value)
                }
            })
        });
        return result;
    }
    
    resetear_inputs(){
        this.my_state.items_list = [];

        this.data.values.forEach(output => {
            const item = this.make_item(output);
            this.registrar_item(item, true);
        });

        this.my_state.items_initialized = true;
        this.mark_dirty();
        this.update_values();
    }

    get_reset_items(){
        this.resetear_inputs();
        return this.my_state.items_list;
    }

    get_default_list(){
        if (!this.my_state.items_initialized) {
            this.resetear_inputs();
        }
        return this.my_state.items_list;
    }

    registrar_item(output,overwrite = false){
        if (this.mismos_items(output.values) && !overwrite) return;
        this.my_state.items_list.push(output);
        this.mark_dirty();
    }


    make_item(output){
        const order_list = this.order_by_cols(output);

        const item_html_key = this.make_key(output.key);
        const item_values = order_list.map(i => ({
            columna: i.key,
            value: i.value,
            unit: i.unit
        }));

        return {
            item_key:output.key,
            values:item_values,
            etiqueta:item_html_key,
        };
    }

    make_key(value){
        let index = 0;
        while (this.my_state.items_list[`${value}_${index}`]){
            index++;
        }
        return `${value}_${index}`;
    }

    mark_dirty(){
        this.needs_update = true;
    }

    update_values(force=false){
        if (!force && !this.needs_update) return false;

        this.needs_update = false;

        this.setStateValue("items_list", this.my_state.items_list);
        // this.setTriggerValue("new", this.my_state.items_list);
        console.log("data_actualizada");
        console.log(this.my_state.items_list);
        
        return true
    }
}
}