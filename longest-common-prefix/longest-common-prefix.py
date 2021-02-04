class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        s = ""
        
        #edge cases if strs = [] or strs ["flower"] or no common prefix
        lst = list(zip(*strs))
        for i,group in enumerate(lst):
            new = set(group)

            if len(new) == 1:
                s = s+new.pop()
            else:
                break

        return s

            
            

            
            
            
            
            


        
        