# rotate the grid and just use re for XMAS and SAMX

import re

# Initialize an empty list to store the grid
grid = []

# Read the text from the file and convert it to a grid
with open("input/day4") as f:
    for line in f:
        grid.append(list(line.strip()))

# unrotated

def count_occurences(grid):

    grid_strings = [''.join(row) for row in grid]
    patterns = [r'XMAS', r'SAMX']
    total_occurrences = 0
    for row in grid_strings:
        for pattern in patterns:
            total_occurrences += len(re.findall(pattern, row))

    print(f"Total occurrences of 'XMAS' and 'SAMX': {total_occurrences}")

count_occurences(grid)

# rotate 90 degrees

grid = [list(row) for row in grid]

# Rotate the grid 90 degrees clockwise
rotated_grid_90 = list(zip(*grid[::-1]))

# Convert the rotated grid back to a list of strings
rotated_grid_90 = [''.join(row) for row in rotated_grid_90]

for row in rotated_grid_90:
    print(row)

count_occurences(rotated_grid_90)

#rotate 45 degrees

grid = [list(row) for row in grid]

# Get the size of the grid
n = len(grid)

# Create a new grid for the rotated result
rotated_grid_45 = [[' ' for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]

# Fill the new grid with the rotated values
for i in range(n):
    for j in range(n):
        rotated_grid_45[i + j][n - 1 + i - j] = grid[i][j]

# Convert the rotated grid back to a list of strings
rotated_grid_45 = [''.join(row) for row in rotated_grid_45]

for row in rotated_grid_45:
    print(row)

count_occurences(rotated_grid_45)

#rotate 135 degrees

# Convert the grid to a list of lists
grid = [list(row) for row in grid]

# Rotate the grid 90 degrees counterclockwise
n = len(grid)
rotated_90_ccw = [[grid[j][n - 1 - i] for j in range(n)] for i in range(n)]

# Create a new grid for the 135 degrees rotated result
rotated_135 = [[' ' for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]

# Fill the new grid with the rotated values
for i in range(n):
    for j in range(n):
        rotated_135[i + j][n - 1 + i - j] = rotated_90_ccw[i][j]

# Convert the rotated grid back to a list of strings
rotated_135 = [''.join(row) for row in rotated_135]

for row in rotated_135:
    print(row)

count_occurences(rotated_grid_45)
