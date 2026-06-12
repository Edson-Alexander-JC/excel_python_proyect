class seccion:
    
    def calc_seccion(self):
        if self.area != 0: return self.area
        self.area = self.frente.b * self.frente.h
        return self.area
    