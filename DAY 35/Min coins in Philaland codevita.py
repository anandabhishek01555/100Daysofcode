# The problem solvers have found a new Island for coding and named it as Philaland. 
# These smart people were given a task to make a purchase of items at the Island easier by distributing various coins with different values. 
# Manish has come up with a solution that if we make coins category starting from Rs.1 till the maximum price of the item present on Island, 
# then we can purchase any item easily. He added the following example to prove his point.

# Lets suppose the maximum price of an item is 5 Rs. then we can make coins of {Rs.1, Rs.2, Rs.3, Rs.4, Rs.5}to purchase any item ranging from Rs.1 till Rs.5.

# Now Manisha, being a keen observer suggested that we could actually minimize the number of coins required and gave following distribution {Rs.1, Rs.2, Rs.3}. According to him any item can be purchased one time ranging from Rs.1 to Rs.5. Everyone was impressed with both of them. Your task is to help Manisha come up with a minimum number of denominations for any arbitrary max price in Philaland.

# Input format
# First line contains an integer T denoting the number of test cases.

# Next T lines contains an integer N denoting the maximum price of the item present on Philaland.

# Output format
# For each test case print a single line denoting the minimum number of denominations of coins required.

# Code constraints
# 1<=T<=100

# 1<=N<=5000

# Sample testcases
# Input  Output 
# 2        4
# 10       3
# 5                

for i in range(int(input())):
    print(len(bin(int(input()))[2:]))

#The logic is just to find the length of binary numbers included in the range for eg.
# 1=1 (len 1)
# 2=10 (len 2)
# 3=11 (len 2)
# 4=100 (len 3)
# 5=101 (len 3) and so on....