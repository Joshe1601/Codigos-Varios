#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define EPSILON 0.00001

void newtonRaphson(double x)
{
	float h_x0;
	float h_xi;
	h_x0 = func(x)/derivFunc(x);
	h_xi = h_x0;
	int i=0;
	float xi=x;
	while (fabs(h_xi) > EPSILON){
		h_xi = func(xi)/derivFunc(xi);
		xi = xi - h_xi;
		i++;
	}
	printf("El valor de la raiz por NewtonRaphson es %f \n El numero de iteraciones es %d\n",xi,i);
}

double func(double x){
	return x*x*x + x - 1;
}
double derivFunc(double x){
	return 3*x*x + 1;
}
