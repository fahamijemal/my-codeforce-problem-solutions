# Read the input word
s = input().strip()

# Count the number of uppercase and lowercase letters
uppercase_count = sum(1 for c in s if c.isupper())
lowercase_count = len(s) - uppercase_count  # total length minus uppercase count

# Convert the word based on the count
if uppercase_count > lowercase_count:
    print(s.upper())
else:
    print(s.lower())
