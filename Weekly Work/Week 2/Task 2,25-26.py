def gcd(p,q):
    while p != q:
        if p>q:
            p = p-q
        if q>p:
            q = q-p
    return p

def lcm(p,q):
    return p*q/(gcd(p,q))

print(lcm(10,6))