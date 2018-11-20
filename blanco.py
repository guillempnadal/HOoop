"""
Define un blanco a ser detectado por un radar
"""

class Blanco(object):

    def __init__(self, coeficiente_reflexion, tiempo_inicial, tiempo_final):
        self.coeficiente_reflexion = coeficiente_reflexion
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final
    
    #Refleja una senal incidente
    def reflejar(self, senal_incidente):
        import senal
        tiempo_inicial = max(senal_incidente.tiempo_inicial,self.tiempo_inicial)
        tiempo_final = min(senal_incidente.tiempo_final,self.tiempo_final)
        amplitud = self.coeficiente_reflexion*senal_incidente.amplitud
        fase=senal_incidente.fase+senal_incidente.frecuencia*(tiempo_inicial-senal_incidente.tiempo_inicial).seconds
        senal_reflejada=senal.Senal(tiempo_inicial,tiempo_final,amplitud,senal_incidente.frecuencia,fase)
        return senal_reflejada
