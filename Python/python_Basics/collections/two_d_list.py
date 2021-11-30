# 2D lists and nested loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# # printing "1" -> in the zeroth (first) row and the
# # zeroth column
# print(number_grid[0][0])
# print(number_grid[2][0])
# # this gives 7, as it's in the third row (index 2)
# # and first (index 0) column

# nested for loop
# we want to select each individual element in the array
for row in number_grid:
    for col in row:
        print(col)
# this prints each element individually (vertically)