class Solution:
    def longestCommonPrefix(self, strs):
        res = ""

        for x in range(len(strs[0])):
            for y in range(1, len(strs)):
                if x==len(strs[y]) or strs[0][x]!=strs[y][x]:
                    return res
            res+=strs[0][x]
        return res


