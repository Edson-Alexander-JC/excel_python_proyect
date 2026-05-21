export default function ({
    parentElement,
    setStateValue,
    setTriggerValue,
    data,
}) {

    const body = parentElement.querySelector(".il-body");
    body.id = data.id

    const main_row = body.querySelector(".row");
    const buttons_row = body.querySelector(".il-buttons-row");
    const inputs_row = body.querySelector(".il-inputs-row");
    const container = body.querySelector(".container");


    const add_btn = buttons_row.querySelector(".add_btn");
    const del_btn = buttons_row.querySelector(".del_btn");
    const reset_btn = buttons_row.querySelector(".reset_btn");

    const inputs = data.value  || [];
    inputs.forEach(element => {
        inputs_row.append(element)
    });
    
    const default_elements = data.values || [];
    default_elements.forEach(element => {
        container.append(element)
    });

    add_btn.onclick = () => {
        var values = [];
            inputs.forEach(element => {
            values.append(element.values)
        });
        element = convert_to_element(values);
        container.append(element);
    }
    del_btn.onclick = () => {
        
    }
    reset_btn.onclick = () => {

    }

    function convert_to_element(datos=[]){

    }



}