#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main( int argc, char *argv[]){
    
    int i,j;
    float **M, **N;
   //printf("\nIngrese las filas1, columnas1");

    int filas1 = atoi(argv[1]);
    int columnas1 = atoi(argv[2]);
    int filas2 = atoi(argv[3]);
    int columnas2 = atoi(argv[4]);

    while (columnas1 != filas2){
        printf("Ha ingresado un número incorrecto de columnas o filas, vuelva a intentarlo:\n");
        scanf("%d %d",&columnas1, &filas2);
    }
    
	
//Datos matriz A
    printf("Matriz A\n" );

    M = (float **)malloc(filas1*sizeof(float*));
   
    for(i=0;i<filas1;i++){
        M[i]= (float *)malloc(columnas1*sizeof(float));
        for(j=0;j<columnas1;j++){
            printf("A(%d,%d)= ",i,j);
            scanf("%f", &M[i][j]);

        }
    }

//Datos matriz B
    printf("Matriz B\n" );

    N = (float **)malloc(filas2*sizeof(float*));
   
    for(i=0;i<filas2;i++){
        N[i]= (float *)malloc(columnas2*sizeof(float));
        for(j=0;j<columnas2;j++){
            printf("B(%d,%d)= ",i,j);
            scanf("%f", &N[i][j]);

        }
    }

//Suma
printf("\n");
printf("Multiplicación de dos matrices\n");
for(i=0;i<filas1;i++){

    int k = 0;
    for(j=0;j<filas2;j++){
        float suma = 0;
        for(k = 0; k <columnas1; k++){
            suma = suma + M[i][k] * N[k][j];

        }
    if (suma == 0){
        continue;
    }else{
        printf( "%.1f\t", suma);
        }
    }

    printf("\n");
}  
    free(M);
    free(M[i]);
    free(N);
    free(N[i]);
    
    return 0;
}