class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [i.lower() for i in s if i.isalnum() == True]
        new = lst.copy()
        
        midpoint = int(len(lst)/2)

        for i in range(midpoint):
            temp = new[i]
            new[i] = new[-i-1]
            new[-i-1] = temp
        
            
        return lst == new
            
            

        