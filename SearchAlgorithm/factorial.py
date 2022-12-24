def recursiveFactorial(n):
    if n > 1:
        return n * recursiveFactorial(n-1)
    else:
        return 1

n = int(input())
factorial = recursiveFactorial(n)
print(factorial)