console.log("STRUCTURE CARGADO");

if (!window.MyApp.ComponentStructure) {

    window.MyApp.ComponentStructure = class {
    
        init(component){
            const {
                parentElement,
                setStateValue,
                setTriggerValue,
                data
            } = component;

            const key = data.key;
            const state = window.MyApp.componets[key];

            if (!state.domain_component) {
                console.log("Nueva Instancia de : " + key);
                state.domain_component = new window.MyApp.DomainComponent();
            }

            this.logic = state.domain_component;
            this.logic.init(component);

            const body = parentElement.querySelector(".il-body");
            this.make_structure(body, data);
            this.def_buttons_events(body, data);
        }

        make_structure(body,data){
            const inputs = data.value.values || [];

            const main_row = document.createElement("div");
            const inputs_row = document.createElement("div");
            const container = document.createElement("div");
            const buttons_row = document.createElement("div");
            const label_contain = document.createElement("div");
            
            main_row.classList.add("row");
            inputs_row.classList.add("il-inputs-row");
            buttons_row.classList.add("il-buttons-row");
            container.classList.add("container");
            label_contain.classList.add("label-contain");

            const add_btn = document.createElement("button");
            const del_btn = document.createElement("button");
            const reset_btn = document.createElement("button");

            add_btn.classList.add("add_btn");
            del_btn.classList.add("del_btn");
            reset_btn.classList.add("reset_btn");

            add_btn.id = "add_btn_" + data.key    
            del_btn.id = "del_btn_" + data.key
            reset_btn.id = "reset_btn_" + data.key    
            
            add_btn.classList.add("il-btn");
            del_btn.classList.add("il-btn");
            reset_btn.classList.add("il-btn");

            add_btn.innerText = "+";
            del_btn.innerText = "-";
            reset_btn.innerText = "reset";
            label_contain.innerText = data.label;

            this.input_row(inputs,inputs_row);
            this.outputs_default(container);

            buttons_row.appendChild(add_btn);
            buttons_row.appendChild(del_btn);
            buttons_row.appendChild(reset_btn);
            
            main_row.appendChild(inputs_row);
            main_row.appendChild(buttons_row);

            body.appendChild(label_contain);
            body.appendChild(main_row);
            body.appendChild(container);
        }

        def_buttons_events(body,data){
            const add_btn = body.querySelector(".add_btn");
            const del_btn = body.querySelector(".del_btn");
            const reset_btn = body.querySelector(".reset_btn");
            const container = body.querySelector(".container");
            const output_group = data.values || [];

            add_btn.onclick = () => {
                this.add_btn(body,container);
                this.logic.update_values();
            };

            del_btn.onclick = () => {
                const key = this.logic.del_btn();
                if(key){
                    body.querySelector(`[data-key="${key}"]`).remove();
                    this.logic.put_target_item(null);
                    this.logic.update_values();
                }
            }

            reset_btn.onclick = () => {this.reset_items(container);}

            this.radio_item_button(body);
        }

        output_row(element){
            const item = document.createElement("div");
            const output_contain = document.createElement("div");
            const unit_contain = document.createElement("div");
            
            item.classList.add("item-contain");
            output_contain.classList.add("output-contain");
            unit_contain.classList.add("unit-contain");

            item.appendChild(output_contain);
            item.appendChild(unit_contain);

            output_contain.innerText = element.value;
            unit_contain.innerText = element.unit;

            return item
        }

        output_item(output){
            const output_item = document.createElement("div");
            output_item.classList.add("radio-item");
            output_item.classList.add("output-item");
            output_item.dataset.key = output.etiqueta;

            output.values.forEach((value)=>{
                const item = this.output_row(value);
                output_item.appendChild(item);
            });
            return output_item;
        }

        input_row(inputs,inputs_row){
            inputs.forEach(e => {
                inputs_row.appendChild(this.input_item(e));
            });
        }

        outputs_default(container){
            container.innerHTML = "";
            const outputs = this.logic.get_default_list();
            Object.values(outputs).forEach(output => {
                container.appendChild(this.output_item(output))
            });
        }

        reset_items(container){
            container.innerHTML = "";
            const outputs = this.logic.get_reset_items();
            Object.values(outputs).forEach(output => {
                container.appendChild(this.output_item(output))
            });
        }

        def_input(element){
            let input;
            if(element.kind === "select"){
                    input = document.createElement("select");
                    element.values.forEach(e_option => {
                        const option = document.createElement("option");
                        option.value = e_option;
                        option.innerText = e_option;
                        input.appendChild(option)
                    });
            }else{
                input = document.createElement("input");
                input.type = element.kind;
                if (element.step){
                    input.step = "any";
                }
            }

            input.dataset.key = element.key;
            if(element.unit){ input.dataset.unit = element.unit;}
            return input
        }

        input_item(element){
            let input = this.def_input(element);

            const label_contain = document.createElement("div");
            const input_contain = document.createElement("div");
            const unit_contain = document.createElement("div");
                
            const input_unit_container = document.createElement("div");
            input_unit_container.appendChild(input_contain);
            input_unit_container.appendChild(unit_contain);

            unit_contain.classList.add("unit-contain");
            label_contain.classList.add("label-contain");
            input_unit_container.classList.add("unit-input");

            const item = document.createElement("div");
            item.appendChild(label_contain);
            item.appendChild(input_unit_container);

            label_contain.innerText = element.label;
            input_contain.appendChild(input);
            unit_contain.innerText = element.unit;

            return item
        }

        add_btn(body,container){
            const inputs_row = body.querySelector(".il-inputs-row");

            const inputs = inputs_row.querySelectorAll("input");
            const selects = inputs_row.querySelectorAll("select");
        
            const new_row = this.logic.add_btn(inputs,selects);

            if(this.logic.update_values()){
                const item = this.output_item(new_row);
                container.appendChild(item);
                this.radio_item_button(body);
            }
        }


        radio_item_button(body){
            body.onclick = (e) => {
                const item = e.target.closest(".radio-item");
                if (!item) return;

                body.querySelectorAll(".radio-item").forEach(el => {
                    el.classList.remove("selected");
                });

                item.classList.add("selected");
                this.logic.put_target_item(item.dataset.key);
            };
        }

    }
}