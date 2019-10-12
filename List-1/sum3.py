# Given an array of ints length 3, return the sum of all the elements.


# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7

def sum3(nums):
	len(nums) == 3
	return sum(nums)
	#for i in range(len(nums)):
		#return nums[i] + nums[i+1] + nums[i+2]
		

print(sum3([5,2,3]))

