# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(int1, int2):
	if (int1 or int2) == 10 or (int1 + int2) == 10:
		return True
	else:
		return False

print(makes10(int1 = 5, int2 = 7))