class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        min_so_far = max_so_far = nums[0]
        result = max_so_far
        
        for i in range(1,len(nums)):
            current = nums[i]
            temp_max = max(current,max_so_far*current,min_so_far*current)
            min_so_far = min(current,max_so_far*current,min_so_far*current)
            
            
            max_so_far = temp_max
            
            result = max(result,max_so_far)
            
        return result
        
        

    
    
    
    
    
    
    
    
    
    
    
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
                
                
                
            
        

            

            

            