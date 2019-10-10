
# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both 
# strings.


# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

def string_match(str1, str2):
	count = 0
	for i in range(min(len(str1), len(str2)-1)):
		if str1[i:i+2] == str2[i:i+2]:
			count+=1
	return count
	

print(string_match(str1 = "aabddeff", str2 = "aabdeeff"))

