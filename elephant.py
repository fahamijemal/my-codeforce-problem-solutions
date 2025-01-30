# Read the input
x = int(input())

# Calculate the number of full 5-steps
full_steps = x // 5

# Calculate the remaining distance
remaining_distance = x % 5

# If there is any remaining distance, add 1 more step
if remaining_distance > 0:
    full_steps += 1

# Output the result
print(full_steps)
