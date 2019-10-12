
# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


# middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

def middle_way(ar1, ar2):
	len(ar1) == 3
	len(ar2) == 3
	for i in range(len(ar1)) and range(len(ar2)):
		return ar1[1], ar2[1]

print(middle_way([1, 2, 3], [4, 5, 6]))
