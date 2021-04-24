class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for item in strs:
            new = ''.join(sorted(item))
            
            if new not in d:
                d[new] = [item]
                
            else:
                d[new].append(item)
                
        result = [v for k,v in d.items()]
        return result
        

        