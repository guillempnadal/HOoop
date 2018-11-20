"""
Define el simulador del Radar
"""

class Radar(object):

    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector

    #Detecta cuantos blancos hay en un medio, en un intervalo de tiempo
    def detectar(self, medio, tiempo_inicial, tiempo_final):
        senal_emitida=self.generador.generar(tiempo_inicial, tiempo_final)
        senales_reflejadas=medio.reflejar(senal_emitida)
        num_blancos=self.detector.detectar(senales_reflejadas)
        return 'Se detectaron %i blancos' % (num_blancos)

    #Plotea la senal emitida y las reflejadas por un medio en un intervalo de tiempo
    def plotear_senal(self, medio, tiempo_inicial, tiempo_final):
        import matplotlib.pyplot as pp
        senal_emitida = self.generador.generar(tiempo_inicial, tiempo_final)
        senales_reflejadas = medio.reflejar(senal_emitida)
        t,s = senal_emitida.tabla(tiempo_inicial)
        a, = pp.plot(t, s)
        for senal_reflejada in senales_reflejadas:
            t,s = senal_reflejada.tabla(tiempo_inicial)
            b, = pp.plot(t, s, color='C1')
        pp.xlabel('Tiempo (segundos)')
        pp.ylabel('Senal')
        pp.legend([a,b], ['Emitida','Reflejada'])
        pp.show()
        pp.close()

