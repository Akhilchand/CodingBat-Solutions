
# Given a string, return a string where for every char in the original, there are two chars.


# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'
def double_char(str):
    str2 = []
    for c in str:
        str2.append(2*c)
        
    return "".join(str2)
		

print(double_char(str = "Akhil"))