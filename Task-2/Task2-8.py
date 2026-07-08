## To count how many even numbers are present in a list

num=0
list=[4,1,2,3]
for i in list:
  if i%2==0:
    num+=1

print(f"The number of even numbers present in the list is {num} ")
