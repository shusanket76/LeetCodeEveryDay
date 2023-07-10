# link='https://leetcode.com/problems/word-break/'
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        table=[False for x in range(len(s)+1)]
        table[0]=True
        for x in range(len(s)+1):

            
            if table[x]==True:
                for y in wordDict:
                    print("hi")
                    print(s[x:x+len(y)],y)
                    if s[x:x+len(y)]==y:
  
                        print("by")
                        table[x+len(y)]=True
        print(table)
        return table[len(s)]