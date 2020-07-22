def gcd(a,b):
    while a!=0:
        a,b = b%a, a
    return b

def modinv(a,b):
    if gcd(a,b)!=1:
        return None
    u1, u2, u3 = 1,0,a
    v1, v2, v3 = 0,1,b
    while v3 != 0:
        q = u3//v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
        return u1 % m
