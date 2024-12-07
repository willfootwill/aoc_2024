import re

# Initialize an empty list to store the grid
grid = []

# Read the text from the file and convert it to a grid
with open("input/day4") as f:
    for line in f:
        grid.append(list(line.strip()))

# Convert each row of the grid to a string
grid_strings = [''.join(row) for row in grid]

# Define the patterns to search for
patterns = [r'XMAS', r'SAMX']

# Function to count occurrences of patterns in a grid
def count_occurrences(grid_strings):
    total_occurrences = 0
    for row in grid_strings:
        for pattern in patterns:
            total_occurrences += len(re.findall(pattern, row))
    return total_occurrences

# Count occurrences in the original grid
total_occurrences = count_occurrences(grid_strings)
print(f"Total occurrences of 'XMAS' and 'SAMX' in original grid: {total_occurrences}")

# Rotate the grid 90 degrees clockwise
rotated_grid_90 = list(zip(*grid[::-1]))

# Convert the rotated grid back to a list of strings
rotated_grid_90_strings = [''.join(row) for row in rotated_grid_90]

# Count occurrences in the 90 degrees rotated grid
total_occurrences_90 = count_occurrences(rotated_grid_90_strings)
print(f"Total occurrences of 'XMAS' and 'SAMX' in 90 degrees rotated grid: {total_occurrences_90}")

# Rotate the grid 45 degrees
n = len(grid)
rotated_grid_45 = [[' ' for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]
for i in range(n):
    for j in range(n):
        rotated_grid_45[i + j][n - 1 + i - j] = grid[i][j]


# Convert the 45 degrees rotated grid back to a list of strings
rotated_grid_45_strings = [''.join(row) for row in rotated_grid_45]
print(rotated_grid_45_strings)
# Count occurrences in the 45 degrees rotated grid
total_occurrences_45 = count_occurrences(rotated_grid_45_strings)
print(f"Total occurrences of 'XMAS' and 'SAMX' in 45 degrees rotated grid: {total_occurrences_45}")

# Rotate the grid 90 degrees counterclockwise
n = len(grid)
rotated_90_ccw = [[grid[j][n - 1 - i] for j in range(n)] for i in range(n)]

# Create a new grid for the 135 degrees rotated result
rotated_grid_135 = [[' ' for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]

# Fill the new grid with the rotated values
for i in range(n):
    for j in range(n):
        rotated_grid_135[i + j][n - 1 + i - j] = rotated_90_ccw[i][j]

# Convert the rotated grid back to a list of strings
rotated_grid_135 = [''.join(row) for row in rotated_grid_135]

# Print the rotated grid
for row in rotated_grid_135:
    print(row)

total_occurrences_135 = count_occurrences(rotated_grid_135)

print(f"Total occurrences of 'XMAS' and 'SAMX' in 135 degrees rotated grid: {total_occurrences_135}")