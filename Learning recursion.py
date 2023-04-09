
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

def printMo


def printMove(fr, to):
  print('move from ' + str(fr) + ' to ' + str(to))
 
def Towers(n, fr, to, spare):
  if n == 1:
    printMove(fr, to)
  else:
    Towers(n-1, fr, spare, to)
    Towers(1, fr, to, spare)
    Towers(n-1, spare, to, fr)

Towers(4, 'fr', 'to', 'spare')


#just to test slicing in python
s = 'wes'
x = s[1:-1]
print(x)
# Now i understand it more 

