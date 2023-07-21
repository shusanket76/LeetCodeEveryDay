class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start = sorted([x[0] for x in intervals])
        end = sorted([y[1] for y in intervals])
        startcount = 0
        endcount = 0
        count=0
        res=0
        while startcount<len(intervals) and endcount<len(intervals):
            if start[startcount]<end[endcount]:
                count+=1
                startcount+=1
            else:
                count-=1
                endcount+=1
            
            res = max(res,count)
        return res
