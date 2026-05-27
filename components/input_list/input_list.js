var items_list = [];
var target_item = null;


export default function (component) {
    const {
        parentElement,
        setStateValue,
        setTriggerValue,
        data
    } = component;

    const body = parentElement.querySelector(".il-body");
    
    if (!body) return;
    if (body.dataset.initialized) return;
    
    body.dataset.initialized = "true";
    body.dataset.key = data.key;

    init(data,body);

}

function init(data,body){
    make_structure(body,data);
    def_buttons_events(body,data);
}

function make_structure(body,data){
    const input_group = data.value || [];
    const inputs = input_group.values || [];
    const output_group = data.values || [];

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

    add_btn.classList.add("il-btn");
    del_btn.classList.add("il-btn");
    reset_btn.classList.add("il-btn");

    add_btn.innerText = "+";
    del_btn.innerText = "-";
    reset_btn.innerText = "reset";
    label_contain.innerText = data.label;

    make_inputs(inputs,inputs_row);
    make_outputs_default(output_group,container);

    buttons_row.appendChild(add_btn);
    buttons_row.appendChild(del_btn);
    buttons_row.appendChild(reset_btn);
    
    main_row.appendChild(inputs_row);
    main_row.appendChild(buttons_row);

    body.appendChild(label_contain);
    body.appendChild(main_row);
    body.appendChild(container);
}

function make_inputs(inputs,inputs_row){
    inputs.forEach(e => {
        inputs_row.appendChild(make_input_item(e));
    });
}

function make_outputs_default(output_group,container){
    output_group.forEach(output_row => {
        make_outputs(output_row,container);
    });
}

function def_input(element){
    let input;
    if(element.kind === "select"){
            input = document.createElement("select");
            element.values.forEach(e_option => {
                const option = document.createElement("option");
                option.value = e_option.value;
                option.innerText = e_option.value;
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

function make_input_item(element){
    let input = def_input(element);

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

function make_output_item(element){
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

function def_buttons_events(body,data){
    const add_btn = body.querySelector(".add_btn");
    const del_btn = body.querySelector(".del_btn");
    const reset_btn = body.querySelector(".reset_btn");

    const container = body.querySelector(".container");

    add_btn.onclick = () => {
        def_add_btn(body,container);
    }

    del_btn.onclick = () => {
        if(!target_item) return;
        items_list[target_item].etiqueta.remove();
        delete items_list[target_item];
        target_item = null;
    }

    reset_btn.onclick = () => {
        items_list = [];
        container.innerHTML = "";
        const output_group = data.values || [];
        make_outputs_default(output_group,container);
    }

    radio_item_button(body);

}

function radio_item_button(body){
    
    const items = body.querySelectorAll(".radio-item");

    items.forEach(item => {
        item.addEventListener("click", () => {

            // quitar seleccion previa
            items.forEach(el => {
                el.classList.remove("selected");
            });

            // seleccionar actual
            item.classList.add("selected");

            // valor seleccionado
            target_item = item.dataset.key
            console.log(item)
            console.log(target_item)

        });

    });
}

function make_outputs(inputs_items,container){
    const output_item = document.createElement("div");
    inputs_items.values.forEach((item) => {
        output_item.appendChild(make_output_item(item));
    });

    add_items(inputs_items,output_item);
    const index = inputs_items.key + "_" + items_list.length;
    output_item.dataset.key = index;
    output_item.classList.add("radio-item");
    output_item.classList.add("output-item");
    container.appendChild(output_item);

}


function add_items(item,etiqueta){
    const index = item.key + "_" + items_list.length;
    if(!items_list[index]){
        items_list[index] = {
            value:item.key,
            values:Object.values(item.values).map(item => ({
                value: item.value,
                unit: item.unit
            })),
            etiqueta:etiqueta
        }
    }
}

function def_add_btn(body,container){
    var new_row = {};
    const inputs_row = body.querySelector(".il-inputs-row");
    const inputs = inputs_row.querySelectorAll("input");
    const selects = inputs_row.querySelectorAll("select");

    const hasEmptyInputs = Array.from(inputs).some(input => {
        // ignorar checkbox
        if(input.type === "checkbox"){
            return false;
        }
        return input.value.trim() === "";
    });
    // verificar selects vacios
    const hasEmptySelects = Array.from(selects).some(select => {
        return select.value.trim() === "";
    });

    if(hasEmptyInputs || hasEmptySelects) return;

    new_row = {
        key: "custom",
        values: [
            ...Array.from(inputs).map(input => ({
                value: input.type === "checkbox"
                    ? input.checked
                    : input.value,
                unit: input.dataset.unit || ""
            })),

            ...Array.from(selects).map(select => ({
                value: select.value,
                unit: select.dataset.unit || ""
            }))
        ]
    };
    make_outputs(new_row,container);
    radio_item_button(body);

}