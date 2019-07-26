from binary_exp import *
#HW 6 Q1
def mil_rab(n,a):
  r = 0
  d = 1
  S = n-1

  while S%2 == 0:
    S = S/2
    r = r + 1

  d = S

  #print r,d

  #code for generating signature
  t = 0
  x = []
  k = binary_exp(a,d,n)
  if k == 1:
    #print("Probably Prime")
    return 1 
  while k != n-1 and t != r:
    x.append(k)
    k = binary_exp(k,2,n)
    t += 1
  x.append(k)
  #print x
  if k == n-1:
    return 1
  else:
    return 0