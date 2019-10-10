# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside 
# and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).


# combo_string('Hello', 'hi') → 'hiHellohi'
# combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'

def combo_string(str1, str2):
	if len(str1) < len(str2):
		return str1 + str2 + str1
	elif len(str2) < len(str1):
		return str2 + str1 + str2

print(combo_string(str1 = "Hello", str2 = "dude"))

# (or)

# def combo_string(str1, str2):
#     s = str1
#     l = str2
      
#     if len(s) > len(l):
#         s, l = l, s
                
#     return s + l + s

# print(combo_string(str1 = "Hello", str2 = "dude"))