class SparseVector:
    def __init__(self, nums):
        self.vec1 = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for x in range(len(self.vec1)):
            res+=self.vec1[x]*vec.vec1[x]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)