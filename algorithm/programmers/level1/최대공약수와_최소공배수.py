def gcd(s, l):
    if l % s == 0:
        return s
    return gcd(l - (l // s) * s, s)

def solution(n, m):
    g = gcd(min(n,m), max(n,m))
    return [g, n * m // g]