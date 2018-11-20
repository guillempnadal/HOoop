"""
Clase que crea senales (ondas armonicas de una duracion determinada)
"""

class Senal(object):

    def __init__(self, tiempo_inicial, tiempo_final, amplitud, frecuencia, fase):
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final
        self.amplitud = amplitud
        self.frecuencia = frecuencia
        self.fase = fase

    #Hace la tabla de valores de la onda, respecto a un origen de tiempo
    def tabla(self, origen_tiempo):
        import math
        Delta_t=2*math.pi/(self.frecuencia*100)
        num_muestras=int((self.tiempo_final-self.tiempo_inicial).seconds/Delta_t)
        t = [(self.tiempo_inicial-origen_tiempo).seconds+i*Delta_t for i in range(num_muestras)]
        s = [self.amplitud*math.sin(self.frecuencia*i*Delta_t+self.fase) for i in range(num_muestras)]
        return t,s
    



        
        
      
