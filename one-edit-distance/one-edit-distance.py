class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
#         if abs(len(s) - len(t)) > 1:
#             return False
#         if s == t:
#             return False
        
#         if len(s) < len(t):
#             for i in range(len(s)):
#                 if s[i] != t[i]:
#                     return s[i:] == t[i+1:]
                
#         elif len(s) < len(t):
#             for i in range(len(t)):
#                 if t[i] != s[i]:
#                     return t[i:] == s[i+1:]
#         else:
#             for i in range(len(s)):
#                 if s[i] != t[i]:
#                     return s[i+1:] == t[i+1:]
        
#         return True
              


        if abs(len(s) - len(t)) > 1:
            return False
        if s == t:
            return False
        
        
        if len(s) < len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    if s[i:] == t[i+1:]:
                        return True
                    else:
                        return False
        
        
        elif len(s) > len(t):
            for i in range(len(t)):
                if t[i] != s[i]:
                    if t[i:] == s[i+1:]:
                        return True
                    else:
                        return False
        else:
            for i in range(len(s)):
                if s[i] != t[i]:
                    if s[i+1:] == t[i+1:]:
                        return True
                    else:
                        return False
                    
        return True 
                    
                    

                
        
                    
                
                    

            
                
            
        