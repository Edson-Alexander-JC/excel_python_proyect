import math
from dataclasses import dataclass
@dataclass
class KPI_Tiempo_Maquinaria():
    h_turno:int = 0
    h_mantenimiento_c:int = 0
    h_mantenimiento_p:int = 0
    
    demoras_operacionales:int = 0
    demoras_ciclo:int = 0
    
    @property
    def demoras_total(self): 
        return math.ceil((self.demoras_ciclo + self.demoras_operacionales)/6)
    @property
    def h_disponibles(self): 
        return self.h_turno - (self.h_mantenimiento_c + self.h_mantenimiento_p)
    
    def calc_h_efectivas(self):
        return self.h_disponibles - self.demoras_total
    
    def calc_h_operativas(self):
        return self.h_disponibles - math.ceil(self.demoras_operacionales/ 60)
        
    def calc_disp_fisica(self):
        return (self.h_disponibles / self.h_turno) * 100
        
    def calc_disp_mecanica(self):
        return (
            (self.h_turno - self.h_mantenimiento_c) 
            / self.h_turno
        )*100
        
    def calc_u_operativa(self):
        return (self.calc_h_operativas()/self.h_disponibles) * 100
    
    def calc_u_efectiva(self):
        return (self.calc_h_efectivas()/self.h_turno) * 100
    
    def aprovechamiento_disponibilidad(self):
        return (self.calc_h_efectivas()/self.h_disponibles) * 100