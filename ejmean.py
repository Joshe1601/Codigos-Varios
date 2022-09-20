import numpy as np
import sys
import statistics
import time
import matplotlib.pyplot as plt

tam = [32,64,128,512,1024, 2048]
lista_1_total = []
lista_2_total = []
lista_3_total = []
lista_4_total = []

for num in tam:
  arreglo = 5*np.random.rand(num)
  iteraciones = 10
  lista_a1 = []
  lista_a2 = []
  lista_a3 = []
  lista_a4 = []
  for it in range(iteraciones):
    # Alternativa 1
    tic1 = time.time()
    suma = 0
    for i in range(num):
      suma = suma + arreglo[i]
    promedio = suma/num
    toc1 = time.time()
    lista_a1.append(1e3*(toc1-tic1))
    #print(promedio)

    # Alternativa 2
    tic2 = time.time()
    suma = sum(arreglo)
    promedio2 = suma/num
    toc2 = time.time()
    lista_a2.append(1e3*(toc2-tic2))
    #print(promedio2)

    # Alternativa 3
    tic3=time.time()
    promedio3 = statistics.mean(arreglo)
    toc3 = time.time()
    lista_a3.append(1e3*(toc3-tic3))
  #print(promedio3)

    # Alternativa 4
    tic4 = time.time()
    promedio4 = np.mean(arreglo)
    toc4 = time.time()
    lista_a4.append(1e3*(toc4-tic4))

    #print(promedio4)
  lista_1_total.append(statistics.median(lista_a1))
  lista_2_total.append(statistics.median(lista_a2))
  lista_3_total.append(statistics.median(lista_a3))
  lista_4_total.append(statistics.median(lista_a4))

# plt.plot(lista_a1,'r-+',lista_a2,'g-+',lista_a3,'b-+',lista_a4,'y-+')
# plt.xlabel("Numero de iteraciones")
# plt.ylabel("Tiempo [ms]")
# plt.grid()
# plt.legend(["Uno","Dos","Tres","Cuatro"])
#plt.savefig("imagen.png",dpi = 50)


SUP1 = [i / j for i,j in zip (lista_3_total, lista_1_total)] 
SUP2 = [i / j for i,j in zip (lista_3_total, lista_2_total)]
SUP3 = [i / j for i,j in zip (lista_3_total, lista_4_total)]


#plt.plot(tam,lista_1_total,'r-+',tam,lista_2_total,'g-+',tam,lista_3_total,'b-+',tam,lista_4_total,'y-+')
#plt.xlabel("Tamaño del vector")
#plt.ylabel("Tiempo [ms]")
#plt.grid()
#plt.legend(["Uno","Dos","Tres","Cuatro"])

plt.plot(tam,SUP1,'r-+',tam,SUP2,'g-+',tam,SUP3,'b-+')
plt.xlabel("Tamaño del vector")
plt.ylabel("SpeedUP")
plt.grid()
plt.legend(["SUP1","SUP2","SUP3"])

plt.show()
