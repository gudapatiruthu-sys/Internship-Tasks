num = int(input("Enter the number for the multiplication table: "))
i = 1
## to print a multiplication table  of a given number 
while i <= 10:
    product = num * i
    print(num, "x", i, "=", product)
    i += 1
