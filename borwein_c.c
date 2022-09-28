#include <math.h>
#include <stdio.h>
#define PI 3.141592653589793

void Borwein_c(double x_0,double y_0,float pi_0,int iteraciones){
    float pi_borwein = pi_0;
    double error = fabs(pi_borwein-PI);
    printf("Iteracion x                y                pi       Error\n");
    printf("0         %lf     %lf       %lf       %lf\n",x_0,y_0,pi_borwein,error);
    pi_borwein = pi_0;
    for (int i=1;i<iteraciones;i++){
        double copia_x = x_0;

        x_0 = (0.5)*(sqrt(x_0)+(1/(sqrt(x_0))));
        y_0 = (1+y_0)*(sqrt(copia_x)/(copia_x+y_0));
        pi_borwein = (pi_borwein*y_0*(1+x_0))/(1+y_0);
        error = fabs(pi_borwein -PI);
        printf("%d         %lf     %lf       %lf       %lf\n",i,x_0,y_0,pi_borwein,error);


    }

}