# Given an array of ints, return the number of 9's in the array.


# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

xrange = range
def array_count9(nums):
	count = 0
	for i in xrange(len(nums)):
		if nums[i] == 9:
			count+=1
	return count

print(array_count9([1, 2, 8, 9, 6, 9, 5, 9]))
