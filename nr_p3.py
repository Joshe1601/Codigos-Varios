import ctypes
import numpy as np
EPSILON=0.00001
def func(x):
	return x*x*x + x - 1
def derivFunc(x):
	return 3*x*x + 1
def newtonRaphson(x):
	h_x0 = func(x)/derivFunc(x)
	h_xi = h_x0
	i=0
	xi=x
	while (np.abs(h_xi) > EPSILON):
		h_xi = func(xi)/derivFunc(xi)
		xi = xi - h_xi
		i=i+1
	print("El valor de la raiz por NewtonRaphson es %f \n El numero de iteraciones es %d\n",xi,i)

if __name__ == '__main__':
    #llamar a la libreria 
    lib = ctypes.CDLL('./nr_p3.so')
    #escoger argumentos de entrada
    lib.newtonRaphson.argtypes = [ctypes.c_double]
    x = -1.5
    
    print("Usando Python :")
    newtonRaphson(x)
    print("Usando C :")
    lib.newtonRaphson(x)
