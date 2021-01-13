class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         dict1 = {}
#         dict2 = {}
#         if len(s) == len(t):
#             for i in range(len(s)):
#                 dict1[s[i]]  = s.count(s[i])
#                 dict2[t[i]] = t.count(t[i])
#             return dict1 == dict2
                
#         else:
#             return False
          return sorted(s) == sorted(t)
        
​
​
​
​
        
