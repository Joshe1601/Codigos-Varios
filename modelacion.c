double modelacion_c(int m){
    int i;
    float suma=0;
    for(i=1;i<=m;i++){
        suma= (double)1/(i*i) + suma;
    }
    return suma;
}