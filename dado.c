

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define random(num) (rand()%num+1)

int main(int argc, char *argv[]){
srand(time(NULL));  
    
    int **M;
    int range = atoi(argv[1]);
    int i;

    printf("¡Suerte!\n\n" );
    M = (int **)malloc(4096*sizeof(int*));
    
    for (i = 0; i<6; i++){
        M[i]= (int*)malloc(4096*sizeof(int));
    }

    for(i=0;i<range;i++){
        int d1, d2, suma;
        d1 = random(6);
        d2 = random(6);
        M[d1-1][d2-1] = M[d1-1][d2-1] + 1 ;
        suma = d1 + d2;
        printf("%d - El resultado de tu lanzamiento fue: %d %d y su suma es: %d\n", i, d1, d2, suma);
    }
    printf("\nEstadísticas:\n\n");

    int n;
    for (n = 0;n < 6; n++){ 
        int j;
        for(j = 0; j < 6; j++){
            printf("%d \t",M[n][j]);
        }
    printf("\n");
    }
    free(M);
    // free(M[i]);
}
