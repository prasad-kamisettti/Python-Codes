#fibonacci series 

def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1] 
    
    fib_series = [0, 1]
    a, b = 0, 1
    
    for i in range(2, n):
        c = a + b
        fib_series.append(c)
        a, b = b, c
    
    return fib_series