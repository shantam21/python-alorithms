def isPalindrome(string):
    temp = string[::-1]
    if temp == string:
        return True
    else:
        return False
isPalindrome('malayalam')