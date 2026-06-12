console.log("INPUT_LIST CARGADO");
window.MyApp = window.MyApp || {};
window.MyApp.componets = window.MyApp.componets || {};

export default function (component) {

    const {
        parentElement,
        setStateValue,
        setTriggerValue,
        data
    } = component;

    const key = data.key;
    if (!window.MyApp.componets[key]){
        window.MyApp.componets[key] = {
            states:{
                init: true,
                structure: false,
                domain: false,
                
            }
        }
    }
    
    const structure = new window.MyApp.ComponentStructure();
    structure.init(component);
}
