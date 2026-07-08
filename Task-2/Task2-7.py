## To find the sum of all numbers from 1 to n using a for loop

num=0
n=int(input("Enter the number"))
for i in range(1,n+1):
  num=num+i

print(f"The sum of all numebrs from 1 to {n} is {num}")
