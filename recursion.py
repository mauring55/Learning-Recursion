
# Recursive

def factorial(n):
  
  if n == 1:
    return 1
  
  else:
    return n * factorial(n-1)
             
 
print (factorial(4))


# Iterative 

def iter_factorial(p):
  
  prod = 1
  
  for i in range (1 , p+1):
    prod *= i
  
  return prod

print (iter_factorial(4))



