class Solution:
    def replaceElements(self, arr):
        rightmax = -1
        for x in range(len(arr)-1, -1,-1):
            newmax = max(rightmax, arr[x])
            arr[x] = rightmax
            rightmax = newmax
        return arr