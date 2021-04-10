class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result = []
        dic = {}
        
        for i,path in enumerate(paths):
            
            lst = path.split(' ')
            
            for j in range(1,len(lst)):
                content = lst[j].split('(')[1].split(')')[0]
                part = (lst[0]+'/'+lst[j]).split('(')[0]

                
                if content not in dic:
                    dic[content] = [part]

                
                else:
                    dic[content].append(part)
        
        for k,v in dic.items():
            if len(v) > 1:
                result.append(v)
                    
        return result

                
                
        
        