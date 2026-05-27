import math
from data.macizo_rocoso import MacizoRocoso
from data.frente_voladura import FrenteVoladura
from data.volquete import Volquete
from data.explosivo import Explosivo
from data.maq_voladura import MaqVoladura

class VoladuraDomain():
    def __init__(self,
        frente,
        roca,
        volquete,
        explosivo,
        maq_voladura,
    ):
        self.frente : FrenteVoladura = frente
        self.roca : MacizoRocoso = roca
        self.volquete : Volquete = volquete
        self.explosivo : Explosivo = explosivo
        self.maq_voladura : MaqVoladura = maq_voladura
        
        self.area: float = 0
        self.volumen: float = 0
        self.burden_konya : float = 0
        pass
    def def_maquinaria(self):
        self.diametro_broca : float = 0
        self.long_barra : float = 0
    

    def calc_seccion(self):
        if self.area != 0: return self.area
        self.area = self.frente.b * self.frente.h
        return self.area
    
    def calc_volumen(self):
        if self.volumen != 0: return self.volumen
        self.volumen = self.calc_seccion() * self.frente.z
        
        return self.volumen
    
    def tonelaje(self) -> float:
        return self.calc_volumen() * self.roca.pe
    
    def volumen_real(self):
        return self.calc_volumen() * self.roca.f_esponjamiento
    
    def calc_r_traccion(self):
        r_traccion = self.roca.ucs/10
        return r_traccion
    
    def calc_p_detonacion(self):
        return 2.5 * self.explosivo.pe *(self.explosivo.vod ** 2) * (10**(-6))
    
    def burden_pearse_1955(self):
        p_det = self.calc_p_detonacion()
        r_tracion = self.calc_r_traccion()
        raiz = (p_det/r_tracion)**(1/2)
        diametro = self.maq_voladura.diametro_broca / 10
        
        burden = self.roca.f_k_roca * diametro
        burden = burden * raiz
        return round(burden,2)
    
    def burden_andersen_1952(self):
        diametro = self.maq_voladura.diametro_broca / 25.4
        long = self.frente.z * 3.28084 
        
        burden = (diametro * long) ** (1/2)
        return round(burden,2)
    
    def burden_fraenkel_1952(self):
        r_voladura = self.roca.f_k_roca
        long_barreno = self.frente.z ** 0.3
        diametro = self.maq_voladura.diametro_broca ** 0.8
        long_epx = (self.explosivo.long_explosivo / 1000) ** 0.3
        
        burden = r_voladura * long_barreno * long_epx * diametro
        return round(burden,2)
    
    def burden_allsman_1960(self,diametro_t,p_det,time_p_det,vel_min,p_esp):
        burden = p_det * diametro_t * time_p_det * (9.8)
        burden = burden / (p_esp * vel_min)
        burden = burden ** (1/2)
        return burden
    def burden_ash_1963(self,f_k_roca,diametro_t):
        burden = (diametro_t * f_k_roca) / 12
        return round(burden,2)

    def burden_konya_1976(self):
        if(self.burden_konya != 0): return round(self.burden_konya,2)
        diametro = self.maq_voladura.diametro_broca
        densidad_exp = self.explosivo.pe
        densidad_roca = self.roca.pe
        
        raiz = (densidad_exp/densidad_roca) ** (1/2)
        self.burden_konya = (diametro / 10) * raiz
        return round(self.burden_konya,2)
    
    def espaciamiento_Konya_1976(self):
        long = self.frente.z
        burden = self.burden_konya
        espaciamiento = 0
        
        r_rigidez = long/burden
        if(r_rigidez < 4):
            espaciamiento = long + (7 * burden)
            espaciamiento = espaciamiento / 8
        else:
            espaciamiento = 1.2 * burden

        return round(espaciamiento,2)
    
    def taco_Konya_1976(self):
        burden = self.burden_konya
        taco = 0.7 * burden
        return round(taco,2)
    
    def f_energia_JKRMC_1986(self):
        rmr = self.roca.f_k_roca  # Tu valor: 70.0
        ucs = self.roca.ucs       # Tu valor: 200.0
        
        # --- CORRECCIÓN CRUCIAL EN ESTA LÍNEA ---
        # No usamos el volumen del frente entero.
        # Estimamos el volumen del bloque unitario a partir del espaciamiento de juntas.
        # Si tu base de datos no tiene la distancia de juntas, se usa 1.0 m³ como estándar JKMRC.
        volumen_bloque_roca = 1.0  
        
        raiz = (ucs / 100) ** (1 / 2)
        mod_young = 10 ** ((rmr - 10) / 40)
        mod_young = mod_young * raiz / 1000
        
        # Aplicamos la regresión del JKMRC con el volumen del bloque
        volumen_ajustado = volumen_bloque_roca * 0.12603
        densidad_roca_ajustado = self.roca.pe * (10 ** (-1)) * (-8.8085)
        mod_young_ajustado = mod_young * (10 ** (-2)) * 1.43294
        ucs_ajustado = ucs * (10 ** (-3)) * 1.34603
        factor_independent = 2.30208
        
        f_energia = (
            volumen_ajustado +
            densidad_roca_ajustado +
            mod_young_ajustado +
            ucs_ajustado +
            factor_independent
        )
        
        f_energia = f_energia * 238.83    
        return round(f_energia, 2)

    def f_carga_JKRMC_1986(self):
        f_energia = self.f_energia_JKRMC_1986()
        # NOTA: energia_exp debe resultar en unidades de kcal/kg
        energia_exp = self.explosivo.calor * self.explosivo.f_potencia
        f_carga = (1000 * f_energia) / energia_exp
        return round(f_carga, 2)
    
    def burden_JKRMC_1986(self):
        """Calcula el burden geométrico real en metros."""
        # Recuperamos el factor de carga (ej: 151.21 g/ton)
        f_carga = self.f_carga_JKRMC_1986() 
        
        # --- CORRECCIÓN CRUCIAL DE UNIDADES ---
        # Como 151.21 está en g/ton, lo dividimos entre 1000 para trabajar en kg/ton
        f_carga_kg = f_carga / 1000  # Dará 0.15121 kg/ton
        
        import math
        # Asumiendo que tu diámetro está en milímetros (ej: 102mm, 152mm)
        # Si ya está en metros en tu clase, quita el '/ 1000'
        diametro_m = self.maq_voladura.diametro_broca / 1000  
        
        # 1. Calcular cuántos kg de explosivo entran por cada metro de taladro
        area_taladro = (math.pi * (diametro_m ** 2)) / 4
        densidad_explosivo_kg_m3 = self.explosivo.pe * 1000  # Ej: 1.2 * 1000 = 1200 kg/m3
        kg_explosivo_por_metro = area_taladro * densidad_explosivo_kg_m3
        
        # Masa total en el taladro (asumiendo columna completa en la altura h)
        masa_explosivo_total = kg_explosivo_por_metro * self.frente.h
        
        # 2. Despeje geométrico del Burden
        h = self.frente.h
        espaciamiento = self.frente.espaciamiento
        densidad_roca = self.roca.pe  # En ton/m3 (ej: 2.8)
        
        # Ahora el denominador usará f_carga_kg (0.15121) en vez de 151.21
        denominador = espaciamiento * h * densidad_roca * f_carga_kg
        burden = masa_explosivo_total / denominador
        
        # Descomenta esto para ver cómo cambian tus prints de control:
        # print("Nuevo Denominador:", denominador)
        # print("Masa Explosivo Total (kg):", masa_explosivo_total)
        # print("Burden Resultante:", burden)
        
        return round(burden, 2)


    def nro_taladros_met_empirico(self,b,h):
        return 10 * ((b*h) ** (1/2))
    def nro_taladros_met_perimetros(self,b,h,f_k_roca,espaciamiento):
        nro_taladros = self.calc_seccion(b,h) ** (1/2)
        nro_taladros = nro_taladros * 4
        nro_taladros = nro_taladros / espaciamiento
        nro_taladros = nro_taladros + (f_k_roca * self.calc_seccion(b,h))
        return nro_taladros
        
            
    def avance_real(self,long_barra,f_arranque,f_perforacion):
        return long_barra * f_arranque * f_perforacion
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