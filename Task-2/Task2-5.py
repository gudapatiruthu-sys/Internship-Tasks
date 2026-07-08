## To find the nth Fibonacci numbers using recursive function

def fibonacci_numbers(N):
  if N<=1:
    return N
  elif N>1:
    return fibonacci_numbers(N-1)+fibonacci_numbers(N-2)

print(fibonacci_numbers(2))
