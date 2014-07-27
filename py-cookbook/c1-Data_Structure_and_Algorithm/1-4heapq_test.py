import heapq

nums = [1,8,3,23,7,-4,18,23,42,37,2]

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
print(sorted(nums)[0:3])
print(sorted(nums)[-3:])

#/*if n is equal to 1, min and max is a better choice*/
