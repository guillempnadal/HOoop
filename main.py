import math
import datetime
import generador
import detector
import radar
import blanco
import medio

def main():

    #Parametros del generador de senales
    amplitud = 0.2
    frecuencia = 0.002
    fase=math.pi/4

    #Parametros de los blancos
    coeficiente_reflexion1 = 0.3
    tiempo_inicial1 = datetime.datetime(2016,3,5,2)
    tiempo_final1 = datetime.datetime(2016,3,5,4)
    coeficiente_reflexion2 = 0.15
    tiempo_inicial2 = datetime.datetime(2016,3,5,5)
    tiempo_final2 = datetime.datetime(2016,3,5,7)
    coeficiente_reflexion3 = 0.5
    tiempo_inicial3 = datetime.datetime(2016,3,5,8)
    tiempo_final3 = datetime.datetime(2016,3,5,13)
    coeficiente_reflexion4 = 0.2
    tiempo_inicial4 = datetime.datetime(2016,3,5,11)
    tiempo_final4 = datetime.datetime(2016,3,5,14)
    
    #Construimos generador de senales y detector
    generador1 = generador.Generador(amplitud,frecuencia,fase)
    detector1 = detector.Detector()

    #Y a partir de ellos hacemos un radar
    radar1 = radar.Radar(generador1,detector1)

    #Creamos algunos blancos
    blanco1 = blanco.Blanco(coeficiente_reflexion1,tiempo_inicial1,tiempo_final1)
    blanco2 = blanco.Blanco(coeficiente_reflexion2,tiempo_inicial2,tiempo_final2)
    blanco3 = blanco.Blanco(coeficiente_reflexion3,tiempo_inicial3,tiempo_final3)
    blanco4 = blanco.Blanco(coeficiente_reflexion4,tiempo_inicial4,tiempo_final4)
    
    #Y con ellos formamos un medio
    medio1=medio.Medio([blanco1,blanco2,blanco3,blanco4])

    #Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    #Medimos
    print(radar1.detectar(medio1,tiempo_inicial,tiempo_final))
    radar1.plotear_senal(medio1,tiempo_inicial,tiempo_final)

if __name__=="__main__":
    main()




