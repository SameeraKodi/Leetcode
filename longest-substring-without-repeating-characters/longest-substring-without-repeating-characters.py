class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr_1 = 0
        ptr_2 = 0
        max_result = 0
        sam = set()

        
        while ptr_2 < len(s):
            if s[ptr_2] not in sam:
                sam.add(s[ptr_2])
                ptr_2 += 1
                max_result = max(max_result,len(sam))
                

            else:
                sam.remove(s[ptr_1])
                ptr_1 += 1
        return max_result
                
            
            
        

                
        