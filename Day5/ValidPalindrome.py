# link = "https://leetcode.com/problems/valid-palindrome/"
def isPalindrome(s):
    newS = ""
    aplha="abcdefghijklmnopqrstuvwxyz0123456789"
    for x in s:
        if x.lower() in aplha:
            newS+=x.lower()

    return(newS==newS[::-1])
a = isPalindrome("A man, a plan, a canal: Panama")