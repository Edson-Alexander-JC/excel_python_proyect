from ..fabric.explosivo import Explosivo
from ..features.voladura.voladura import Voladura
from ..fabric.carguio import Carguio
from ..features.perforacion.perforacion import Perforacion
from ..features.labor.labor_fabric import LaborFabric


class MinaForms():
    def get_forms():
        return {
                "Labor": LaborFabric(),
                "Perforacion": Perforacion(),
                "Voladura": Voladura(),
                "Carguio": Carguio(),
            }