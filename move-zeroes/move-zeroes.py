class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = nums.count(0)
        nums[:]=[i for i in nums if i != 0 ]
        for i in range(n):
            nums.append(0)
        return nums

