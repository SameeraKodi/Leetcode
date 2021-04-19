class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_without = max_neg = max_pos = nums[0]
        for i in range(1, len(nums)):
            max_without = max(max_pos, max_without)
            if nums[i] < 0:
                max_neg, max_pos = min(max_pos * nums[i], nums[i]), max_neg * nums[i]
            else:
                max_neg, max_pos = max_neg * nums[i], max(max_pos * nums[i], nums[i])
        return max(max_without, max_pos)
    
    
    
    
    
    
    
    
    
    
    
    
#             max_product = nums[0]
#         left = 0
        
#         while left < len(nums):
#             #print("left",left)
            
#             current_prod = nums[left]
#             prod = [current_prod]
#             for i in range(left+1,len(nums)):
#                 current_prod = current_prod*nums[i]
#                 #print("current-prod",current_prod)
#                 prod.append(current_prod)
#             #print("prod",prod)
                
#             max_product = max(max_product,max(prod))
#             left += 1
#             #print("max",max_product)
            
#         return max_product
                
                
                
            
        

            

            

            