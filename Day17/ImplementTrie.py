# link="https://leetcode.com/problems/implement-trie-prefix-tree/description/"
class TrieNode:
    def __init__(self):
        self.children={}
        self.endofWord=False


class Trie(object):

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr=self.root
        for x in word:
            if x not in curr.children:
                curr.children[x] = TrieNode()
            curr=curr.children[x]
        curr.endofWord=True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr=self.root
        for x in word:
            if x not in curr.children:
                return False
            else:
                curr= curr.children[x]
        return curr.endofWord
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for x in prefix:
            if x not in curr.children:
                return False
            curr = curr.children[x]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)