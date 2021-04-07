class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if len(intervals ) == 0:
            return True
        intervals.sort()
        

        
        for j in range(1,len(intervals)):
            print(j)
            if intervals[j][0] > intervals[j-1][0] and intervals[j][0] < intervals[j-1][1]:
                return False

            elif intervals[j][1] > intervals[j-1][0] and intervals[j][1] < intervals[j-1][1]:
                return False

            elif intervals[j][0] == intervals[j-1][0] and intervals[j][1] == intervals[j-1][1]:
                return False
            else:
                    continue
        return True
                 
            
            
        
        

        
        
        
        