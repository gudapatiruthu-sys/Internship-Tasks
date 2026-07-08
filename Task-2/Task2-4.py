##To check if a number is prime (Scalable version)
def checking_number(number):
    if number <= 1:
        return f"The number {number} is neither prime nor composite"
    
    # Loop from 2 up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return f"The number {number} is not a prime number"
            
    return f"The number {number} is a prime number"

print(checking_number(121))
