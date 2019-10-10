
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.


# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(int1, int2):
	if int1 == int2:
		return 2*(int1 + int2)
	else:
		return int1 + int2

print(sum_double(int1 = 7, int2 = 7))
