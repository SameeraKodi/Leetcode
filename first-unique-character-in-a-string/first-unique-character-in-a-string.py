class Solution:
    def firstUniqChar(self, s: str) -> int:
        lst = [s.index(l)  for l in set(s) if s.count(l)==1]
        return min(lst) if len(lst)>0 else -1
​
        
​
​
​
​
​
        
        
