M = 1000000007

  
def exponentiation(bas, exp): 
    t = 1; 
    while(exp > 0):  
        if (exp % 2 != 0): 
            t = (t * bas) % M; 
  
        bas = (bas * bas) % M; 
        exp = int(exp / 2); 
    return t % M; 
  


t = input()
for inp in range(t):
	k = input()
	r = 2
	power = exponentiation(2, k - 1)
	print (10 * power ) % M