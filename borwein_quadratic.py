import ctypes
import time
import math

def py_borwein(x_0,y_0,pi_0,iteraciones):
    error =  abs(pi_0 -math.pi)
    iteraciones =4
    print("Iteracion  x                 y               pi                         error")
    print("0       ",round(x_0,6),"           ",round(y_0,6),"                   ",round(pi_0,6),"        ",error)
    pi_borwein = pi_0
    for i in range(1,iteraciones):
        copia_x = x_0
        x_0 = (pow(x_0,1/2)+(1/(pow(x_0,1/2))))/2
        y_0 = (1+y_0)*pow(copia_x,1/2)/(copia_x+y_0)
        pi_borwein = pi_borwein*y_0*(1+x_0)/(1+y_0)
        error = abs(pi_borwein -math.pi)
        print (i,"      ",x_0," ",y_0,"  ",pi_borwein,error)

if __name__=='__main__':
    #llamar a la libreria 
    lib = ctypes.CDLL('./borwein_c.so')
   # escoger argumentos de entrada
    lib.Borwein_c.argtypes = [ctypes.c_double,ctypes.c_double,ctypes.c_float,ctypes.c_int]

    x_0 = pow(2,1/2)
    y_0 = 0
    pi_0 = 2 + pow(2,1/2)
    iteraciones = 4

    print("Usando Python :")
    py_borwein(x_0,y_0,pi_0,iteraciones)
    print("Usando C :")
    lib.Borwein_c(x_0,y_0,pi_0,iteraciones)
