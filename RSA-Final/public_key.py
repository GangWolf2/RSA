import random
from mil_rab import *
from gcd import *

def public_key(m):

  p = random.randint(2**15, 2**16)
  while mil_rab(p,2) != 1:
    p = random.randint(2**15, 2**16)
  
  q = random.randint(2**15, 2**16)
  while mil_rab(q,2) != 1:
    q = random.randint(2**15, 2**16)

  n = p * q


  return (p,q,n)


