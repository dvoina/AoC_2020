def gcd(a: int, b: int) -> int:
    if a==0 or b==0:
        return a + b
    if a==b:
        return a
    if a>b:
        return gcd(a-b,b)
    if b>a:
        return gcd(a, b-a)

print(gcd(27,0))

