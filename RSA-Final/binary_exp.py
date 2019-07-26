def binary_exp(a,e,n):
  if (e == 0):
    return 1
  elif (e%2 == 0):
    return binary_exp(a, e/2, n)** 2 % n
    # ((a**(e/2)) % n)**2 return binary_exp(a, e/2, n)**2
  else: 
    return a * binary_exp(a, e-1, n) % n
      # a * a**(e-1) % n