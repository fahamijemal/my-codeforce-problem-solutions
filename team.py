# Read the number of problems
n = int(input())

# Initialize a counter
solvable_count = 0

# Process each problem's input
for _ in range(n):
    a, b, c = map(int, input().split())  # Read three integers
    if a + b + c >= 2:  # Check if at least two friends are sure
        solvable_count += 1

# Print the final count of solvable problems
print(solvable_count)
