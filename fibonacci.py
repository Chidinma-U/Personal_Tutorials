stored = {0:0, 1:1}

def fibonacci_dynamic (n):
    if n in stored:
        return stored [n]
    else:
        stored [n] = fibonacci_dynamic(n-2)+fibonacci_dynamic(n-1)
        return stored [n]


def fibonacci_recursive (n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive (n-2) + fibonacci_recursive (n-1)
