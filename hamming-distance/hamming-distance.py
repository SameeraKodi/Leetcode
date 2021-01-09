class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        x1 = "{0:b}".format(x)
        x2 = "{0:b}".format(y)
        
​
        diff = abs(len(x1)- len(x2))
        if len(x1) < len(x2):
            x1 = str("0"*diff)+x1
        else:
            x2 = str("0"*diff)+x2
​
        return len([1 for i in range(len(x1)) if x1[i] != x2[i]])
​
​
​
            
​
​
        
​
​
​
                
        
