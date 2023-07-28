class Solution:
    def searchMatrix(self, matrix: [[int]], target: int):
        rl = 0
        rr = len(matrix)-1
        row=0
        while rl<=rr:
            mid = int((rl+rr)/2)
            if matrix[mid][0]<=target and matrix[mid][len(matrix[mid])-1]>=target:
                row = mid
                break
            if matrix[mid][0]>target:
                rr=rr-1
            else:
                rl+=1
        cl = 0
        cr = len(matrix[row])-1
        while cl<=cr:
            mid = int((cl+cr)/2)
            if matrix[row][mid]==target:
                return True
            if matrix[row][mid]<target:
                cl+=1
            else:
                cr-=1
        return False