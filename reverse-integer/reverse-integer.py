class Solution:
    def reverse(self, x: int) -> int:
        temp = str(x)
        temp = temp[::-1]
        if temp[-1] == '-':
            temp = temp[:-1]
            temp = -1*int(temp)
        else:
            temp = int(temp)
        if temp>= 2**31 or temp<= -2**31:
            return 0
        else:
            return temp
​
        
