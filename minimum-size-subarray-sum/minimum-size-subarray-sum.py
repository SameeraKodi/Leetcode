class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums) + 1
        s = 0
        left = 0
        
        for i in range(left,len(nums)):
            s += nums[i]
            
            while s >= target:
                result = min(result,i+1-left)
                s -= nums[left]
                left += 1
                
        return result if result != len(nums) +1 else 0

                
            
        
        