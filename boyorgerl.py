# Read the username as input
username = input().strip()

# Count distinct characters using a set
distinct_chars = set(username)

# Determine gender based on the count of distinct characters
if len(distinct_chars) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
