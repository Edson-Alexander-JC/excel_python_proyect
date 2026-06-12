def nro_taladros_met_empirico(self):
    b = self.frente.b
    h = self.frente.h
    nro_taladros = 10 * ((b*h) ** (1/2))
    return round(nro_taladros, 0)

def nro_taladros_met_perimetros(self):
    espaciamiento = self.frente.espaciamiento
    f_k_roca = self.roca.f_k_roca
    b = self.frente.b
    h = self.frente.h
    perimetro = 0

    if(self.frente.kind == "M.Superficial"):
        perimetro = (2 * b) + (2 * h)
    else:
        perimetro = (self.calc_seccion() ** (1/2)) * 4
    
    nro_taladros = (perimetro / espaciamiento) + (f_k_roca / self.calc_seccion())
    nro_taladros = nro_taladros + (f_k_roca * self.calc_seccion())
    return round(nro_taladros, 0)

def avance_real(self):
    f_perforacion = (self.frente.z/self.maq_voladura.long_barra)
    av = (
            self.frente.z * 
            self.explosivo.f_arranque * 
            f_perforacion
        )
def metros_perforados_por_disp(self,b,h,f_k_roca,espaciamiento,long_barra,f_arranque,f_perforacion):
        nro_tem = self.nro_taladros_met_empirico(b,h)
        nro_tpe = self.nro_taladros_met_perimetros(b,h,f_k_roca,espaciamiento)
        return [
            nro_tem * self.avance_real(long_barra,f_arranque,f_perforacion),
            nro_tpe * self.avance_real(long_barra,f_arranque,f_perforacion),
        ]

def disp_totales(self,long_barra,f_arranque,f_perforacion,z):
    return z / self.avance_real(long_barra,f_arranque,f_perforacion)

def metros_totales_perforados(self,b,h,f_k_roca,espaciamiento,long_barra,f_arranque,f_perforacion):
    nro_tem = self.nro_taladros_met_empirico(b,h)
    nro_tpe = self.nro_taladros_met_perimetros(b,h,f_k_roca,espaciamiento)
    return [
        nro_tem * self.avance_real(long_barra,f_arranque,f_perforacion),
        nro_tpe * self.avance_real(long_barra,f_arranque,f_perforacion),
    ]
