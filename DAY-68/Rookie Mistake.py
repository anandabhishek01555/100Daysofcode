# You’re given a string containing letters of three types, R, B, and ..

# R represents your current position, B represents a blocked position, and . represents an empty position. In one step, you can move to any adjacent position to your current position, as long as it is empty. Can you reach either the leftmost position or the rightmost position?

# Return true if you can reach either the leftmost or the rightmost position, or false if you cannot.

# Example 1
# Input

# s = "......B....R.............."
# Output

# True

s=input()
for i in range(len(s)):
    if s[i]=="R":
        pos=i
x1=s[:pos]
x2=s[pos:]
if "B" not in x1 or "B" not in x2:
        print("True")
else:
    print("False")