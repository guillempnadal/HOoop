class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos

    #Los blancos del medio reflejan una senal
    def reflejar(self, senal):
        senales_reflejadas = []
        for blanco in self.blancos:
            senal_reflejada = blanco.reflejar(senal)
            #Solo guardo la senal reflejada si empieza antes de terminar
            if senal_reflejada.tiempo_inicial<senal_reflejada.tiempo_final:
                senales_reflejadas.append(senal_reflejada)
        return senales_reflejadas
