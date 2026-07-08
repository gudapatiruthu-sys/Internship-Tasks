# To create a Pyramid shape
rows = 4
for i in range(1, rows + 1):
    # Calculate the number of stars (1, 3, 5, 7)
    stars = 2 * i - 1
    # Calculate the spaces needed to center them
    spaces = rows - i
    
    print(" " * spaces + "*" * stars)
