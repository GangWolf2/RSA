public static int binary_exp(int a, int e, int n){
    if(e == 0){
        return 1;
    }
    else if(e%2 == 0){
        return binary_exp(a, e/2, n) ** 2 % n;
    }
    else{
        return a* binary_exp(a,e-1,n) % n;
    }

}