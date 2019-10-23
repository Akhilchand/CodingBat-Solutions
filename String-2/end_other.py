
# Given two strings, return True if either of the strings appears at the very end of the other string, 
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
# Note: s.lower() returns the lowercase version of a string.


# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(str1, str2):
	str1 = str1.lower()
	str2 = str2.lower()
	if str1.endswith(str2) or str2.endswith(str1):
		return True
	else:
		return False
print(end_other(str1 = "Hiabc", str2 = "abc"))