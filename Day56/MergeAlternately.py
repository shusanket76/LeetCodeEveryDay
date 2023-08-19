class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1l = 0
        word2l=0
        news = ""
        while word1l<len(word1) and word2l<len(word2):
            news+=word1[word1l]
            news+=word2[word2l]
            word1l+=1
            word2l+=1
        if word1l<len(word1):
            news+=word1[word1l:]
        if word2l<len(word2):
            news+=word2[word2l:]
        return news