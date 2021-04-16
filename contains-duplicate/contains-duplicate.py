class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        new_l = len(list(set(nums)))
        
        return l != new_l
        