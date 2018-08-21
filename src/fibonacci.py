def fibonacci(n):
    f = 0
    if n <= 1:
        f = n
    else :
        f = fibonacci(n-1) + fibonacci(n-2)
    return f

x = int(input("input a number: "))
print(fibonacci(x))