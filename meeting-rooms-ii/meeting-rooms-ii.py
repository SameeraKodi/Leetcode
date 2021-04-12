class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        count = 1
        if len(intervals) == 0:
            return 0
        
        start,end = list(list(zip(*intervals))[0]),list(list(zip(*intervals))[1])
        start.sort()
        end.sort()

        
        end_ptr = 0
        
        for st_ptr in range(1,len(start)):
            if start[st_ptr] >= end[end_ptr]:
                end_ptr += 1
            else:
                count +=1
                
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(intervals) == 0:
#             return 0
        
#         start,end = list(list(zip(*intervals))[0]),list(list(zip(*intervals))[1])

#         start.sort()
#         end.sort()
#         count = 1

#         end_ptr = 0
        
#         for st_ptr in range(1,len(start)):
#             if start[st_ptr] >= end[end_ptr]:
                
#                 end_ptr += 1
#             else:
#                 count += 1
                
#         return count
    
            
            
        



            
            
        



            
            
                

        return count

                