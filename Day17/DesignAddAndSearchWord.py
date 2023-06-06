# link="https://leetcode.com/problems/design-add-and-search-words-data-structure/description/"

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False



class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for x in word:
            ste = x
            if x  not in curr.children:
                curr.children[ste]=TrieNode()
            
            curr = curr.children[ste]
        curr.endOfWord = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(i,root):
            curr=root
           
            for x in range(i,len(word)):
                if word[x]==".":
                    for child in curr.children.values():
                        if dfs(x+1,child):
                            return True
                    return False

                    
                else:
                    if word[x] not in curr.children:
                        return False
                    curr=curr.children[word[x]]
            return  curr.endOfWord
        return dfs(0,self.root)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)