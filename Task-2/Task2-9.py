## To print all prime numbers between 1 to 100
print("Prime numbers:")
for num in range(1, 101):
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1
    if divisors == 2:
        print(num, end=" ")
