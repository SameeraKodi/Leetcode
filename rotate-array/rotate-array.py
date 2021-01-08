class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
​
        if k > len(nums):
            t = k%len(nums)
            nums[:] = nums[-t:]+nums[:-t]
        else:
            nums[:] = nums[-k:]+nums[:-k]
        
        return nums
        
