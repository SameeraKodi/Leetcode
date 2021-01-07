class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = set(nums)
        nums.sort()
        return len(nums)
        
        
        
