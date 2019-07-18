public static int miller_rabin(int n, int a){
    int r = 0;
    int d = 1;
    int S = n-1;

    while(S%2 == 0){
        S = S/2;
        r += 1;
    }

    d = S;

    int t = 0;

    int [] x;

    int k = binary_exp(a,d,n);

    if (k==1){
        return 1;
    }

    while(k != n-1 && t != r){
        x.add(k);
        k = binary_exp(k,2,n);
        t += 1;
    }

    x.add(k);

    if(k == n-1){
        return 1;
    }
    else{
        return 0;
    }
}