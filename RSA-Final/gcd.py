def gcd(a,b):
 
 #divsteps is variable used to hold the total number of division steps that are required to reach gcd
 # divsteps = 0
 #See Stein Algorithm 1.1.13, states "if a = b, output a and terminate"
  if(a == b):
      return a
  #See Stein Algorithm 1.1.13, states "if b = 0, we output a"
  if(b == 0):
    return a
  #While we can assume that both a,b > 0 based off of Alg 1.1.13, this case prevents from running into issue
  #while(a != 0 and b != 0) loop so program can work with negatives
  while(a != 0 and b > 0):
      #Based off of Lemma 1.1.9 and HW ?2, which states gcd(a,b)= gcd(b, a%b)
      (a,b) = (b, a%b)
      #every time while loop iterates, divsteps will be increased by one to show total number of division steps needed
      #divsteps += 1
  
  #print divsteps
  return a
  