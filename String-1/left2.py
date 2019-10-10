# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string 
# length will be at least 2.


# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(str):
	len(str) >= 2
	return str[2:len(str)+1] + str[:2]

print(left2(str = "Akhil"))