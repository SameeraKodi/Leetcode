class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        if string[0] == "-":
            num = int(string[::-1][:-1])*-1
            
            return num if num > -2**31 else 0
        else:
            num = int(string[::-1])
            return num if num < 2**31 else 0
            
        