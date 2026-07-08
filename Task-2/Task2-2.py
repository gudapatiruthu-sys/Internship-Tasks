##To accept three numbers and returns the largest one 
def largest_one(a,b,c):
  if a>b and a>c:
    return f"The number {a} is the largest one" 
  elif b>a and b>c:
    return f"The number {b} is the largest one"
  else:
    return f"The number {c} is the largest one"

print(largest_one(5,10,15))
