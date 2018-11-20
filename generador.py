"""
Un generador de senal es el responsable de generar una senal portadora.
"""

class Generador(object):

    def __init__(self,amplitud,frecuencia,fase):
        self.amplitud = amplitud
        self.frecuencia = frecuencia
        self.fase = fase

    def generar(self,tiempo_inicial,tiempo_final):
        import senal
        senal1 = senal.Senal(tiempo_inicial,tiempo_final,self.amplitud,self.frecuencia,self.fase)
        return senal1
