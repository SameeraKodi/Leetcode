class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        running_sum = nums[0]
        max_sum = nums[0]
        
        for i in nums[1:]:
            running_sum  = max(running_sum+i,i)
            max_sum = max(max_sum,running_sum )
    

        return max_sum          
            
            

        
        