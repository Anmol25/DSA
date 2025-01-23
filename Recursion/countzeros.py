def czeros(n):
    if n == 0:
        return 0
    
    last_digit = n % 10

    ans = 0

    if last_digit == 0:
        ans = 1

    ans_rest = czeros(n//10)

    return ans + ans_rest


print(czeros(10305))
