# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last 
# element. Both arrays will be length 1 or more.


# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

def common_end(ar1, ar2):
	len(ar1) >= 1
	len(ar2) >= 1
	for i in range(len(ar1)) and range(len(ar2)):
		if ar1[0] == ar2[0]:
			return True
		elif ar1[-1] == ar2[-1]:
			return True
		else:
			return False

print(common_end([1, 2, 5], [2,4,5]))