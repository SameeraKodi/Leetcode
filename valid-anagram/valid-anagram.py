class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #method 1 ( slow)
#         dict1 = {}
#         dict2 = {}
#         if len(s) == len(t):
#             for i in range(len(s)):
#                 dict1[s[i]]  = s.count(s[i])
#                 dict2[t[i]] = t.count(t[i])
#             return dict1 == dict2
                
#         else:
#             return False
​
        #method 2
        #return sorted(s) == sorted(t)
        
        #method 3 
        dict1 = {}
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for j in t:
            
            if j not in dict1:
                return False
            else:
                dict1[j] -= 1
        for val in dict1.values():
            if val != 0:
                return False
​
        return True
                
            
         
        
​
​
​
​
        
