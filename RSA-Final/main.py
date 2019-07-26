import random
from mil_rab import *
from binary_exp import * 
from euler_phi import *
from xgcd import * 
from gcd import *

def RSA(m):

  #example value p = 17
  p = random.randint(2**12, 2**13) #no issues
  while mil_rab(p, 2) != 1:
    p = random.randint(2**12, 2**13)
    #pPrime == True

  # example value q = 19
  q = random.randint(2**20, 2**21) #no issues
  while mil_rab(q,2) != 1:
   q = random.randint(2**20, 2**21)
    #qPrime == True

  n = p * q #no issues
  print "Public Key n: " + str(n)

  secretD = euler_phi(p,q) #no issues
  print "Euler D: " + str(secretD)

  d = -1

  while(d < 0): #can remove this and program will work with infinite recursion however
    e = random.randint(2**20, 2**21)
    print("e: " + str(e))

    while gcd(e, secretD) != 1:
      e = random.randint(2**20, 2**21)
      print("New e: " + str(e))

    d = xgcd(e, secretD)[1]
    print("D: " + str(d))

  c = binary_exp(m,e,n)
  print ("C: " + str(c))

  decrypt = binary_exp(c,d,n) 


  print m, decrypt

print RSA(4297281437)
         #1111111 after this length the program breaks, but still less than 9,999,999
         #to consistently work, value tested must be below 2,000,000
         #can work above that value, but not consistently

         #reason RSA stopped working was due to restrictions placed on the RNG for p,q, and the resulting n. A rule of RSA is that the m<n in all cases, meaning m can only exist in the range of 0 thru n-1. The issue wasn't so much the math and calculations as it was the input I was entering. The program works fine, but becuase of the generation restrictions on p,q, the value of n could only get so large before the m outpaced it and caused the number generation to generate n values that were consistently lower than the m value, causing the modular division to not work correctly (decrypt). Since m was larger than n, actual modular division was occuring which would return the remainder of m/n instead of m itself. In modular division, m%n would return m since m<n, no remainder can exist. So, for future reference, if you want to increase the input number, make sure to increase the p and q and e values, maybe make the range for p and q an input
