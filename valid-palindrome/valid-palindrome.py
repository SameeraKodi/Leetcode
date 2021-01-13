class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst =[i for i in s.lower() if i.isalnum()]
        
#         for i in s.lower():
#             if i.isalnum():
#                 lst.append(i)
​
        return lst == lst[::-1]
​
        
