# Read the input
s = input().strip()

# Split the string by '+' to extract the numbers
numbers = s.split('+')

# Sort the numbers
numbers.sort()

# Join the numbers back with '+' and print the result
print('+'.join(numbers))
