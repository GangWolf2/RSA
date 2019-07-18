public static int xgcd(int a, int b){
    int x, y, r, s = 1,0,0,1;

    if(b == 0){
        return (a,x,y);
    }

    while(b>0){

        int quo = a/b;
        int rem = a%b;

        (a,b,r,s,x,y) = (b, rem, x-quo * r, y - quo * s, r, s)
    }

    return(a,x,y);
}