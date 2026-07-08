Int1=int(input("Enter the first number"))
Int2=int(input("Enter the second  number"))
Int3=int(input("Enter the third number"))

if (Int1>Int2 and Int1>Int3):
  print("The First number is greater than both the numbers")

elif (Int2>Int1 and Int2>Int3):
  print("The Second number is greater than both the numbers")

elif (Int3>Int2 and Int3>Int1):
  print("The Third number is greater than both the numbers")

else:
  print("There is no single largest number")
