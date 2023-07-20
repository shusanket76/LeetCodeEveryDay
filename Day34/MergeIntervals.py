class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        for y in range(1,len(intervals)):
            
            anchor = intervals[y]
            j=y-1
            print(intervals[j][0])
            while j>=0 and anchor[0]<intervals[j][0]:
                intervals[j+1]=intervals[j]
                j=j-1
            intervals[j+1] = anchor
        
            
        res=[]
        x=1
        while x<len(intervals):
            if intervals[x-1][1]<intervals[x][0]:
                res.append(intervals[x-1])
            else:
                intervals[x]=[min(intervals[x-1][0], intervals[x][0]), max(intervals[x-1][1], intervals[x][1])]
            x=x+1
        res.append(intervals[x-1])
        return res