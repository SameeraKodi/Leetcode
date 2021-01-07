class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        end = {}
        for i,val in enumerate(nums):
            x = target - val
            if x not in end:
                end[val] = i
            else:
                return [end[x],i]
​
        
