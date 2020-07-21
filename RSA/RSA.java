import java.util.Scanner;
import java.lang.Math;

public class RSA{

    public static void Main(string args []){

    int p = Math.random(2**10, 2**11);

    while (miller_rabin(p,2) != 1){
        p = Math.random(2**10, 2**11);
    }

    int q = Math.random(2**10, 2**11);
    while (miller_rabin(q,2) != 1){
        q = Math.random(2**10, 2**11);
    }

    int n = p * q;

    int secretD = eulerPhi(p,q);
    System.out.println("Euler D: " + secretD);

    int e = Math.random(2**10, 2**11);
    System.out.println("E: " + e);

    while(gcd(e, secretD) != 1){
        e = Math.random(2**10, 2**11);
    }

    int d = xgcd(e, secretD);

    int c = binary_exp(m, e, n);

    int decrypt = binary_exp(c,d,n);

    System.out.println("Encrypted Number: " + m + "Decrypted number: " decrypt);



    }

}
