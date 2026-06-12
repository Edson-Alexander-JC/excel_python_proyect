from app_module.interfaces.input_item import InputItem
class DemorasGlobal():
    def get_demoras():
        return [
            InputItem(key="cambio_turno",
            values=[
                InputItem(value="Cambio de turno"),
                InputItem(value=15),
            ]),
            InputItem(key="charla_seguridad",
            values=[
                InputItem(value="Charla de seguridad"),
                InputItem(value=25),
            ]),
        ]