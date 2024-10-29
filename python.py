import math
import time

def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
        
def sieveF(N):
    if N < 2:
        return False
    
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    
    for num in range(2, int(N**0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, N + 1, num):
                sieve[multiple] = False
                
    return sieve[N]

def fermat(n, k=5):
    if n <= 1:
        return False
    if n == 2: return True
    if n % 2 == 0:
        return False
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        
        if pow(a, n - 1, n) != 1:
            return False

def miller_rabin(n, k = 5):
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

n = 1

k = 10
r = 1

avr = 0
result = None

for i in range(r):
    start = time.time()
    result = isPrime(n)
    avr += time.time()-start
    
avr /= r

avr2 = 0
result2 = None

for i in range(r):
    start = time.time()
    result2 = sieveF(n)
    avr2 += time.time()-start
    
avr2 /= r

avr3 = 0
result3 = None

for i in range(r):
    start = time.time()
    result3 = fermat(n)
    avr3 += time.time()-start
    
avr3 /= r

avr4 = 0
result4 = None

for i in range(r):
    start = time.time()
    result4 = miller_rabin(n)
    avr4 += time.time()-start
    
avr4 /= r