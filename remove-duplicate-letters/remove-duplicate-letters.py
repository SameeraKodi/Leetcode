class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack = []
        
        #seen? this lets us keep track of whats in our solution : for O(1) time
        seen = set()
        
        #last occurence to know if there are more ocurrences of s[i] in s
        last_occurrence = {c:i for i,c in enumerate(s)}
        
        for i,d in enumerate(s):
            if d not in seen:
                while stack and d < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                
                seen.add(d)
                stack.append(d)
                
        return ''.join(stack)

                
        

                
        
                
                
            
        