class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
#         lst1 = [i for i in s].sort()
#         lst2 = [j for j in t].sort()
        
        return sorted(s) == sorted(t)
 
            
         
        




        