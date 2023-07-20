def canAttendMeetings(intervals):
    for x in range(1, len(intervals)):
        anchor = intervals[x]
        j=x-1
        while j>=0 and anchor[0]<intervals[j][0]:
            intervals[j+1]=intervals[j]
            j=j-1
        intervals[j+1] = anchor
    
    for y in range(1,len(intervals)):
        if intervals[y-1][1]>intervals[y][0]:
            return False
        
    return True




# a = canAttendMeetings([[0,30],[5,10],[15,20]])
b= canAttendMeetings([[7,10],[2,4]])
print(b)