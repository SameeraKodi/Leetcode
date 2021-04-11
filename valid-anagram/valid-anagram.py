class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        
        if len(s) != len(t):
            return False
        
        dict_1 = {}
        #dict_2 = {}
        

        for i in range(len(s)):
            if s[i] not in dict_1:
                dict_1[s[i]] = 1
            else:
                dict_1[s[i]] +=1
                
        for j in range(len(t)):
            if t[j] not in dict_1:
                return False
            else:
                dict_1[t[j]] -= 1

        return all(x== 0 for x in dict_1.values())
 
        
#         for k in range(len(t)):
#             if t[k] not in dict_2:
#                 dict_2[t[k]] = 1
#             else:
#                 dict_2[t[k]] +=1
                
#         return dict_1 == dict_2
                
        
            
            
            
            
        
        
        
        
        
#         if len(s) != len(t):
#             return False
        
#         return sorted(s) == sorted(t)
    
    #solution using hash map
        
    
    
    
 
            
         
        




        