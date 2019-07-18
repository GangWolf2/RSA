public static int gcd(int a, int b){
    if(a == b){
        return a;
    }
    if(b == 0){
        return a
    }

    while(a != 0 && b > 0){
        a = b;
        b = a%b;
    }

    return a;
}