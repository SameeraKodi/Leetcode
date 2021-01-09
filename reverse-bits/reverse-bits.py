class Solution:
    def reverseBits(self, n: int) -> int:
​
        x = '{:032b}'.format(n)
        l = x[::-1]
        #print(int(l,2))
        return int(l,2)
​
​
​
        
        
