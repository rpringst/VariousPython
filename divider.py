def factorize(n, primes):
    factorlist = []
    for p in primes:
        if p*p > n:
            break
        i = 0
        while n%p == 0:
            n//=p
            i+=1
        if i > 0:
            factorlist.append((p, i));
    if n > 1:
        factorlist.append((n, 1))
    return factorlist

def divisors(f):
    divisorlist = [1]
    for (p, r) in f:
        divisorlist = [d * p**e for d in div for e in range(r + 1)]
    return divisorlist
