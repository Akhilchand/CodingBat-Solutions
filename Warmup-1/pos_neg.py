
# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is 
# True, then return True only if both are negative.


# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True

def pos_neg(int1, int2, negative):
	if (int1 > 0 and int2 < 0) and not negative:
		return True
	elif (int1 < 0 and int2 > 0) and not negative:
		return True
	elif (int1 < 0 and int2 < 0) and negative:
		return True
	else:
		return False

print (pos_neg(-1, -1, False))