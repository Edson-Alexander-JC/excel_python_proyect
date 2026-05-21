from interfaces.every_put_interface import EveryPutInterface
from data.input_item import InputItem
textinput = EveryPutInterface()

# dataset: InputItem = InputItem(
#     kind="string",label="label",key="key_string",unit="$",value = "valor"
# )
# textinput.input_normal(dataset)
# dataset: InputItem = InputItem(
#     kind="number",label="label",key="key_nro_int",unit="$",value = 520
# )
# textinput.input_normal(dataset)
# dataset: InputItem = InputItem(
#     kind="float",label="label",key="key_nro_float",unit="$",value = 5.84
# )
# textinput.input_normal(dataset)
# dataset: InputItem = InputItem(
#     kind="select",label="label",key="key_select",unit="$",values = [
#         ("dsl", "Diesel"),
#         ("gas", "Gasolina"),
#         ("elec", "Eléctrico")
#     ]
# )
# textinput.input_normal(dataset)
dataset: InputItem = InputItem(
    kind="list",key="key_select",
    value=InputItem(
        "Inputs",
        "key_input",
        values= [
            InputItem("string","key_string_in_input_list",width=0.3),
            InputItem("number","key_number_in_input_list",unit="$"),
            InputItem("float","key_float_in_input_list",unit="$"),
            InputItem("select","key_select_in_input_list",
                      values=["asda","asdsad0",541,5.5],width=0.4
            ),
        ]
    ),
    values = [
        #ITEM1
        InputItem("list", values= [
            InputItem("string",value="y"),
            InputItem("number",value=850),
            InputItem("float",value=1.5),
            InputItem("select",value=["OP2"]),
        ]),#ITEM2
        InputItem("list", values= [
            InputItem("string",value="x"),
            InputItem("number",value=880),
            InputItem("float",value=1.65),
            InputItem("select",value=["OP1"]),
        ]),#ITEM3
        InputItem("list", values= [
            InputItem("string",value="z"),
            InputItem("number",value=0),
            InputItem("float",value=2.5),
            InputItem("select",value=["OP3"]),
        ]),#ITEM4
        InputItem("list", values= [
            InputItem("string",value="e"),
            InputItem("number",value=550),
            InputItem("float",value=5.2),
            InputItem("select",value=["OP4"]),
        ])
    ]
)
textinput.render_input(dataset)