class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char =="(" or char =="[" or char =="{":
                stack.append(char)
            elif stack: 
                prev_char = stack.pop()
                if prev_char == "(" and char != ")":
                    return False
                
                    
                elif prev_char == "{" and char != "}":
            
                    return False
                elif prev_char == "[" and char != "]":
                    return False

            else:
                return False
                
        return len(stack) == 0

                    
                                    
        

                
                
                
        