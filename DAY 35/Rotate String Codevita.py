
# Rotate a given String in the specified direction by specified magnitude. 
# After each rotation makes a note of the first character of the rotated String, 
# After all, rotation are performed the accumulated first character as noted previously will form another string, say FIRSTCHARSTRING. 
# Check If FIRSTCHARSTRING is an Anagram of any substring of the original string. If yes print "YES" otherwise "NO". 

# Input format
# The first line contains the original string s.
# The second line contains a single integer q.
# The ith of the next q lines contains character d[i] denoting direction and integer r[i] denoting the magnitude.

# Output format
# If yes print "YES" otherwise "NO".

# Code constraints
# 1 <= Length of original string <= 30

# 1<= q <= 10

# Sample testcases
# Input 1
# carrace
# 3
# L 2
# R 2
# L 3

word = 'FIRSTCHARSTRING'
commands = [
  ('L', 2),
  ('R', 3),
  ('L', 1),
]

from collections import deque

q = deque(word)

for direction, magnitude in commands:
  if direction == 'L':
    q.rotate(-magnitude)
  else:
    q.rotate(magnitude)

if ''.join(q) == word:
    print('Yes')
else:
    print('No')