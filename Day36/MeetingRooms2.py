def minMeetingRooms(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort()
        for x in range(1,len(intervals)):
            if intervals[x-1][1]>intervals[x][0]:
                