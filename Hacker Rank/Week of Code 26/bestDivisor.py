#!/usr/bin/python3

n = int(input().strip())

divisors = [x for x in range(1,n+1) if n % x == 0]
bestDivisor = 1

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True    

for i in divisors:
    if i < 10 and i > bestDivisor:
        bestDivisor = i
    else:
        temp = i
        s = 0
        while temp != 0:
            s += temp % 10
            temp /= 10
        if s > bestDivisor and i < bestDivisor and not(is_prime(n)):
            bestDivisor = i
        elif s > bestDivisor and is_prime(n):
            bestDivisor = i

print(int(bestDivisor))
        
