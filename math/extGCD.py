def extGCD(a, b):
    """ax+by=gcd(a, b)を満たすx, yの組を返す"""
    if b == 0:
        return a, 1, 0
    d, y, x = extGCD(b, a%b)
    y -= (a//b)*x
    return d, x, y

# ex)
# 37x+101y = gcd(37, 101)
# extGCD(37, 101) => (1, -30, 11)
# 37*(-30) + 101*11 = 1 
