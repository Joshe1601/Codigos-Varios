import numpy as np
import ctypes
import time
import statistics
import matplotlib.pyplot as plt


def modelacion_py(m):
    suma=0
    for i in range(1,m+1):
        suma= 1/pow(i,2) + suma
    return suma

#print(type(modelacion_py(5)))

if __name__=='__main__':
    #llamar a la librería
    lib = ctypes.CDLL('./modelacion.so')
    #Escoger el tipo de argumento de entrada 
    lib.modelacion_c.argtypes= [ctypes.c_int] #para float cómo sería
    #Escoger el tipo de argumento de salida
    lib.modelacion_c.restype = ctypes.c_double
    pi= np.pi
    
    #tiempos1=[]
    #tiempos2=[]
    #tiempo_m1=[]
    #tiempo_m2=[]
    m_py=1
    inicio1= time.time()    
    while True:
        #inicio1= time.time()
        valor_estimado = modelacion_py(m_py)
        #final1= time.time()
        #tiempos1.append(1e6*(final1-inicio1))
        valor_real= pow(pi,2)/6
        x_py= (valor_estimado/valor_real)

        if x_py>=0.99:
            ##Pipipipipi: (6*valor_estimado)**(1/2)
            print('El valor de pi es:',m_py)
            break
        
        m_py= m_py + 1
    final1= time.time()
    tiempo_python= 1e6*(final1-inicio1)
    print('El tiempo en Python es:',tiempo_python)
    #tiempo_m1.append(statistics.median(tiempos1))

    m_c=1
    inicio2= time.time()
    while True:
        #inicio2= time.time()
        valor_estimado= lib.modelacion_c(m_c)
        #final2= time.time()
        #tiempos2.append(1e6*(final2-inicio1))
        valor_real= pow(pi,2)/6
        x_c= (valor_estimado/valor_real)
        #print(x_c)
        if x_c>=0.99:
            print('El valor de pi es:',m_c)
            break
        m_c= m_c+1
    final2= time.time()
    tiempo_c= 1e6*(final2-inicio2)
    print('El tiempo en C es:',tiempo_c)
    #tiempo_m2.append(statistics.median(tiempos2))

    
    
    #print(tiempo_m1)
    #print(tiempo_m2)

SUP1= tiempo_python/tiempo_c
#SUP1 = [i / j for i,j in zip (tiempo_m2,tiempo_m1)]
#plt.plot(numeros,SUP1)

names = ['Speedup 1']
values = [50]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(SUP1, values)

plt.suptitle('Gráfico de barras')
plt.show()
