# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

n = int(input("Enter the value for n: "))
diff21 = int(input("Enter the value for diff21: "))
if diff21 == 21:
	print (diff21 - n)
elif diff21 > 21:
	print (2*int(diff21 - n))