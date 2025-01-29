# Read input
n, t = map(int, input().split())
queue = list(input().strip())

# Simulate t seconds
for _ in range(t):
    i = 0
    while i < len(queue) - 1:
        if queue[i] == 'B' and queue[i + 1] == 'G':
            # Swap B and G
            queue[i], queue[i + 1] = queue[i + 1], queue[i]
            i += 1  # Skip the next position to prevent double swap
        i += 1

# Convert list back to string and print result
print("".join(queue))
