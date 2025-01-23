def sum_digits(n: int):
    if n <= 0:
        return 0
    
    last_digit = n % 10

    sum_rest = sum_digits(n//10)

    return last_digit + sum_rest 


print(sum_digits(1111))