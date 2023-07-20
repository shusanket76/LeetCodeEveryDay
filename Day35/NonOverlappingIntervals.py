class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # for x in range(1, len(intervals)):
        #     anchor = intervals[x]
        #     j=x-1
        #     while j>=0 and anchor[0]<intervals[j][0]:
        #         intervals[j+1]= intervals[j]
        #         j=j-1
        #     intervals[j+1]= anchor
        intervals.sort()
        y=1
        count = 0
        while y<len(intervals):
            if intervals[y-1][1]>intervals[y][0]:
                count+=1
                if intervals[y-1][1]>intervals[y][1]:
                    intervals.remove(intervals[y-1])
                else:
                    intervals.remove(intervals[y])
                y-=1
            y+=1
        return count
