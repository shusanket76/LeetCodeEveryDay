class Solution:
    def isAlienSorted(self, words, order):
        hasmap = {}
        for x in range(len(order)):
            hasmap[order[x]] = x
        for a in range(len(words)-1):
            w1,w2 = words[a], words[a+1]
            for b in range(len(w1)):
                if b==len(w2):
                    return False
                if w1[b]!=w2[b]:
                    if hasmap[w1[b]]>hasmap[w2[b]]:
                        return False
                    break
        return True