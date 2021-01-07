class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        end = []
        for i,val in enumerate(nums):
            x = target - val
            if x in nums and nums.index(x) != i and i not in end:
                end.append(i)
                end.append(nums.index(x))
        return end
        
