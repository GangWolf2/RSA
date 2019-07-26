def xgcd(a,b):
  # initialize values
  (x, y, r, s) = (1, 0, 0, 1)
  if(b == 0):
    return (a, x, y)
  while(b > 0):
    #set quotient and remainder
    quo = a / b
    rem = a % b
    # now do the recursion
    (a, b, r, s, x, y) = (b, rem, x - (quo* r), y - (quo * s), r, s)
  return (a,x,y)

