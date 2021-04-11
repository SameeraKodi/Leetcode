class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        #2 pointer method
        begin = 0
        end = len(s)-1
        
        while begin <= end:
            temp = s[begin]
            s[begin] = s[end]
            s[end] = temp
            begin += 1
            end -= 1
        
        
        
        
        
        
        
        """
        Do not return anything, modify s in-place instead.
        """
#         l = len(s)
#         mid_len = int(len(s)/2)
        
# #         if mid_len%2 == 0:
#         for i in range(mid_len):
            
#             temp = s[i]
#             s[i] = s[l-(i+1)]
#             s[l-(i+1)] = temp
            
#         return s

       
            
        