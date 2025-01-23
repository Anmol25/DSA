def count(n : int):
    if n == 0:
        return 0
    
    ans = count(n//10)

    return ans + 1

print(count(123))