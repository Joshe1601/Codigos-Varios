import ctypes
import time
import math

###### FUNCIÓN GAUSS - LEGENDRE EN PYTHON #######
def py_Gauss(a_0,b_0,t_0,iteraciones):
    
    pi_Gauss=pow(a_0+b_0,2)/(4*t_0)
    error=abs(pi_Gauss-math.pi)
    print("Iteration  a         b         t        pi               Error")
    print("0         ",round(a_0,6),"       ",round(b_0,6),"",t_0,"   ",round(pi_Gauss,14),error)
    
    for i in range(1,iteraciones):
      copia_a=a_0
      a_0=(1/2)*(a_0+b_0)
      b_0=pow(copia_a*b_0,1/2)
      t_0=t_0-pow(2,i-1)*pow(a_0-copia_a,2)
      pi_Gauss=pow(a_0+b_0,2)/(4*t_0)
      error=abs(pi_Gauss-math.pi)
      print(i,"        ",round(a_0,6),"",round(b_0,6),"",round(t_0,6),round(pi_Gauss,14),error)


###### FUNCIÓN BORWEIN QUADRATIC EN PYTHON #######
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


###### FUNCIÓN BORWEIN QUINTIC EN PYTHON #######
def py_quintic(a_0,s_0,iteraciones):
  x_0 = y_0 = z_0 = 0
  pi_quintic = 0
  error = abs(pi_quintic-math.pi)
  print("Iter      x              y            a           s            pi                Error")
  print(f"0            {round(x_0,8)}            {round(y_0,2)}         {round(a_0,8)}          {round(s_0,3)}          {round(pi_quintic,10)}           {round(error,8)}")
  

  for i in range(1, iteraciones):

    x_0 = (5/s_0)-1
    y_0 = pow(x_0-1, 2)+7
    z_0 = pow(0.5*x_0*(y_0 + math.sqrt(pow(y_0,2)-4*pow(x_0,3))), 0.2)
    a_0 = pow(s_0,2)*a_0 - pow(5,i-1)*((pow(s_0,2)-5)/2 + math.sqrt(s_0*(pow(s_0,2)-2*s_0+5)))
    s_0 = 25/(pow(z_0 + x_0/z_0 + 1, 2)*s_0)
    pi_quintic = 1/a_0
    error = abs(pi_quintic -math.pi)
    print(f"{i}        {round(x_0,8)}     {round(y_0,2)}      {round(a_0,8)}     {round(s_0,3)}     {round(pi_quintic,10)}       {round(error,8)}")



###### FUNCIÓN GAUSS - LEGENDRE EN C #######
if __name__ == '__main__':  #def main():#main()
    #llamar a la libreria
    lib =ctypes.CDLL('./c_Gauss.so')
    #escoger argumentos de entrada
    lib.Gauss_c.argtypes = [ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_int]
    #escoger el tipo de argumento de salida
    
    a_0=1
    b_0=1/(pow(2,1/2))
    t_0=0.25
    iteraciones=4
    
    print("Utilizando el programa en Python:")
    py_Gauss(a_0,b_0,t_0,iteraciones)
    
    print("")
    print("Utilizando el programa en C:")
    lib.Gauss_c(a_0,b_0,t_0,iteraciones)
    


###### FUNCIÓN BORWEIN QUADRATIC EN C #######
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


###### FUNCIÓN BORWEIN QUADRATIC EN C #######
if __name__=='__main__':
    #llamar a la libreria 
    lib = ctypes.CDLL('./quintic_c.so')
   # escoger argumentos de entrada
    lib.Quintic_c.argtypes = [ctypes.c_double,ctypes.c_double,ctypes.c_int]

    a_0 = 0.5
    s_0 = 5*(math.sqrt(5)-2)
    iteraciones = 4

    print("Usando Python :")
    py_quintic(a_0,s_0,iteraciones)
    print("Usando C :")
    lib.Quintic_c(a_0,s_0,iteraciones)


    # n_iter = []

    # time_Gauss_py =[]
    # time_quad_py = []
    # time_quintic_py = []

    # time_Gauss_c =[]
    # time_quad_c = []
    # time_quintic_c = []

    # for i in range(10):

    #   start = time.perf_counter()
    #   py_Gauss(a_0,b_0,t_0,iteraciones)
    #   end = time.perf_counter()
    #   time_Gauss_py.append(start-end)
    #   n_iter.append(i)
      
    # print(time_Gauss_py)

    # for i in range(10):

    #   start = time.perf_counter()
    #   lib.Gauss_c(a_0,b_0,t_0,iteraciones)
    #   end = time.perf_counter()
    #   time_Gauss_c.append(start-end)

    # print(time_Gauss_c)

    # for i in range(10):

    #   start = time.perf_counter()
    #   py_borwein(x_0,y_0,pi_0,iteraciones)
    #   end = time.perf_counter()
    #   time_quad_py.append(start-end)

    # print(time_quad_py)

    # for i in range(10):

    #   start = time.perf_counter()
    #   lib.Borwein_c(x_0,y_0,pi_0,iteraciones)
    #   end = time.perf_counter()
    #   time_quad_c.append(start-end)

    # print(time_quad_c)

    # for i in range(10):

    #   start = time.perf_counter()
    #   py_quintic(a_0,s_0,iteraciones)
    #   end = time.perf_counter()
    #   time_quad_py.append(start-end)

    # print(time_quintic_py)

    # for i in range(10):

    #   start = time.perf_counter()
    #   lib.Quintic_c(a_0,s_0,iteraciones)
    #   end = time.perf_counter()
    #   time_quad_c.append(start-end)


    # print(time_quintic_c)
  


