# Read the input strings
string1 = input().strip().lower()
string2 = input().strip().lower()

# Compare the strings lexicographically
if string1 < string2:
    print("-1")
elif string1 > string2:
    print("1")
else:
    print("0")
