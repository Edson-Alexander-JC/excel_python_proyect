from ..fabric.explosivo import Explosivo
from ..fabric.frente_voladura import FrenteVoladura
from ..fabric.carguio import Carguio
from ..features.perforacion.perforacion import Perforacion
from ..features.labor.labor_fabric import LaborFabric


class SuperficialForms():
    def get_forms():
        return {
                "Labor": LaborFabric(),
                "Perforacion": Perforacion(),
                "Voladura": FrenteVoladura(),
                "Explosivo": Explosivo(),
                "Carguio": Carguio(),
            }