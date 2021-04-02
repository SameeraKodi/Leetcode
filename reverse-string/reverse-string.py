class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        mid_len = int(len(s)/2)
        
#         if mid_len%2 == 0:
        for i in range(mid_len):
            
            temp = s[i]
            s[i] = s[l-(i+1)]
            s[l-(i+1)] = temp
            
        return s
            
        