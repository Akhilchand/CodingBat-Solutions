# Given an int array length 2, return True if it contains a 2 or a 3.


# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has23(arr):
	len(arr) == 2
	for i in range(len(arr)):
		if 2 in arr or 3 in arr:
			return True
		else:
			return False

print(has23([1, 2]))