def gsum(n):
    if n == 0:
        return 1
    
    ans = 1/(2**n)

    rest = gsum(n-1)

    return ans + rest

print(gsum(3))