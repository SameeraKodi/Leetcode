class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(current_sum + nums[i],nums[i])
            max_sum = max(current_sum,max_sum)
            
        return max_sum
#have two sums : one for current sum and one for the global sum


        
        
#         current_sum = nums[0]
#         max_sum = nums[0]
        
#         for i in nums[1:]:
#             current_sum  = max(current_sum+i,i)
#             max_sum = max(max_sum,current_sum )
    

#         return max_sum
