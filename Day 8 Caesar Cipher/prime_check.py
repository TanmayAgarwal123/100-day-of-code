import math
def prime_checker(number):
  prime = True
  for i in range(2,int(math.sqrt(number))):
    if(number%i==0):
      prime=False
  if(prime==True):
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
n = int(input())
prime_checker(number=n)