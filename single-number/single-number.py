class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        while len(nums) >1:
            if nums[0] == nums[1]:
                nums.pop(0)
                nums.pop(0)
                
​
            else:
                return nums[0]
        return nums[0]
        
        
