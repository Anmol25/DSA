def print_n(n : int):
    if n == 0:
        return
    
    print_n(n-1)
    
    print(n, end = " ")

print_n(20)

print("")