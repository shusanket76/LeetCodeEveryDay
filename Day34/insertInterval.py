
def insert(intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        x = 0
        res=[]
        while x<len(intervals):
            if intervals[x][0]>newInterval[1]:
                res.append(newInterval)
                return res+intervals[x:]
            elif intervals[x][1]<newInterval[0]:
                res.append(intervals[x])
            else:
                newInterval=[min(intervals[x][0], newInterval[0]), max(intervals[x][1], newInterval[1])]
            x+=1
        res.append(newInterval)
        return res
a = insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])
print(a)