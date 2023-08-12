# link = "https://leetcode.com/problems/valid-palindrome/"
def isPalindrome(s):
    newS = ""
    aplha="abcdefghijklmnopqrstuvwxyz0123456789"
    for x in s:
        if x.lower() in aplha:
            newS+=x.lower()

    return(newS==newS[::-1])
# # ====================SOL-2==================================+++?
#     class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l=0
#         r=len(s)-1
#         alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
#         while l<r:
#             while l<r and  s[l].lower() not in alpha:
#                 l+=1
#             while l<r and s[r].lower() not in alpha:
#                 r-=1
#             if s[l].lower()!=s[r].lower():
#                 return False
#             l+=1
#             r-=1
#         return True

a = isPalindrome("A man, a plan, a canal: Panama")