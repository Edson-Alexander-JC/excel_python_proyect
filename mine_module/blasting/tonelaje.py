class Tonelaje():    
    def tonelaje(self) -> float:
        return self.calc_volumen() * self.roca.pe
    
    def volumen_real(self):
        return self.calc_volumen() * self.roca.f_esponjamiento
    