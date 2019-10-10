# Given a string, return the count of the number of times that a substring length 2 appears in the string and 
# also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

xrange = range
def last2(str):
    if len(str) < 2:
        return 0
          
    
    end = str[len(str)-2:]
    count = 0
                
    for i in xrange(len(str) - 2):
    	if str[i] == str[i+1]:
        	count+=1     

    return count

print(last2(str = "abbcc"))
