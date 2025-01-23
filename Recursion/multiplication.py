def mul(m: int,n: int):
    if (n == 0):
        return 0
    
    ans = mul(m,n-1)

    return m + ans

print(mul(4,3))