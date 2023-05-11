import re


def isValidSSN(str):
    regex = "^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$"
    
    p  = re.compile(regex)
    
    if (str == None):
        return False
    
    if (re.search(p, str)):
        return True
    else:
        return False
    
# Test Case 1:
str1 = "856-45-6789"
print(isValidSSN(str1))
 
# Test Case 2:
str2 = "000-45-6789"
print(isValidSSN(str2))
 
# Test Case 3:
str3 = "856-452-6789"
print(isValidSSN(str3))
 
# Test Case 4:
str4 = "856-45-0000"
print(isValidSSN(str4))