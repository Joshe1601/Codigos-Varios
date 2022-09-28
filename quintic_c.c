#include <math.h>
#include <stdio.h>
#define PI 3.141592653589793

void Quintic_c(double a_0,double s_0,int iteraciones){
    double x_0, y_0, z_0;
    float pi_quintic;
    double error = fabs(pi_quintic-PI);
    printf("Iter      x              y            a            s             pi                 Error\n");
    printf("0       %lf     %lf      %lf     %lf        %lf          %lf\n",x_0,y_0,a_0,s_0,pi_quintic,error);

    for (int i=1;i<iteraciones;i++){

        x_0 = (5/s_0)-1;
        y_0 = pow(x_0-1, 2)+7;
        z_0 = pow(0.5*x_0*(y_0+sqrt(pow(y_0,2)-4*pow(x_0,3))), 0.2);
        a_0 = pow(s_0,2)*a_0 - pow(5,i-1)*((pow(s_0,2)-5)/2 + sqrt(s_0*(pow(s_0,2)-2*s_0+5)));
        s_0 = 25/(pow(z_0 + x_0/z_0 + 1, 2)*s_0);
        pi_quintic = 1/a_0;
        error = fabs(pi_quintic -PI);
        printf("%d       %lf     %lf     %lf     %lf       %.10lf       %.10lf\n", i, x_0, y_0, a_0, s_0, pi_quintic, error);
    }

}

