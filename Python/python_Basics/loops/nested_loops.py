# nested loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iteration of the "outer loop"

rows = int(input("How many rows?: ")) # we're working with numbers
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

# drawing a rectangle using a symbol
for i in range(rows):
    for j in range(columns):
        print(symbol, end="") # end will prevent the cursor from going to the next line
    print()
