# Given a string, return a new string where the first and last chars have been exchanged.


# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(word):
	if len(word) <= 1:
		return word
	else:
		l = list(word)
		l[0], l[-1] = l[-1], l[0]
		new_str = ''.join(l)
		return new_str

print(front_back(word = "a"))