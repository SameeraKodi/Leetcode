class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = "{0:b}".format(n)
        count = 0
        for i in num:
            if i == '1':
                count += 1
        return count
​
        
