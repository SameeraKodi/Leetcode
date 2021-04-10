class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        result = 100000
        if len(nums) == 0:
            return 0
        
        running_sum = 0
        
        p1 = 0

        
        for i in range(p1,len(nums)):
            running_sum += nums[i]

            
            while running_sum >= target:
                result = min(result,i+1-p1)
                running_sum -= nums[p1]
                p1 += 1
        return result if result != 100000 else 0
                
            
        
        