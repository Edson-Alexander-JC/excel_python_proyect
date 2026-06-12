from app_module.shared.tiempos_maquinaria import TiemposMaquinaria
from app_module.shared.energia_otros_maquinaria import EnergiaOtrosMaquinaria
from app_module.shared.accesorios_maquinaria import AccesoriosMaquinaria

class MaquinariaMiniForms():
    def __init__(self):
        self.tiempos : TiemposMaquinaria = TiemposMaquinaria()
        self.energia : EnergiaOtrosMaquinaria = EnergiaOtrosMaquinaria()
        self.accesorios : AccesoriosMaquinaria = AccesoriosMaquinaria()
    
    def set_maquinaria(self,maq_name):
        self.tiempos.set_maquinaria(maq_name)
        self.energia.set_maquinaria(maq_name)
        self.accesorios.set_maquinaria(maq_name)
        
    def set_tiempos(self,items=[]):
        self.tiempos.render_tiempos(items)
    def set_energia(self,energia=0,lubricante=0,aceite=0):
        self.energia.render_energia(energia,lubricante,aceite)
    def set_accesorios(self,items=[]):
        self.accesorios.render_accesorios(items)