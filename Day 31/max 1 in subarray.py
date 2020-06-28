nums=[1,0,1,0,1,1]
l = 0
r = 0
maxl = 0
for num in nums:
    if num == 1:
        l += 1
    else:
        maxl = max(l+r, maxl)
        r = l
        l = 0
maxl = max(l+r, maxl)
maxl = min(maxl, len(nums)-1) #avoid all 1s array
print(maxl)