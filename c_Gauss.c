#include <math.h>
#include <stdio.h>


void Gauss_c(double a_0,double b_0,double t_0,int iteraciones){
    double pi_Gauss=pow(a_0+b_0,2)/(4*t_0);
    double error= fabs(pi_Gauss-3.141592653589793);
    printf("Iteration  a         b         t        pi               Error \n");
    printf("0          %.6lf  %.6lf  %.6lf %.14lf %lf\n",a_0,b_0,t_0,pi_Gauss,error);
    double copia_a;
    int i;
  
    for (i=1;i<iteraciones;i++){
        copia_a=a_0;
        a_0=(0.5)*(a_0+b_0);
        b_0=sqrt(copia_a*b_0);
        t_0=t_0-pow(2,i-1)*pow(a_0-copia_a,2);
        pi_Gauss=pow(a_0+b_0,2)/(4*t_0);
        error= fabs(pi_Gauss-3.141592653589793);
        printf("%d          %.6lf  %.6lf  %.6lf %.14lf %lf\n",i,a_0,b_0,t_0,pi_Gauss,error);
    }
}