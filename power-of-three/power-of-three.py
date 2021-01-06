class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        new = n
​
        while new%3 == 0 and new!= 0 :
            new = new/3
​
​
        return new==1
