class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))
        # nums.sort()
        # for i in range(len(nums)):
        #     if i <= (len(nums)-1):
        #         return nums[i] == nums[i+1]
        #         break
​
        
        
