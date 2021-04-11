class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #with division:
        prod = 1
        
        for i in nums:
            if i !=0:
                prod = prod*i
            else:
                prod = prod
        
        if nums.count(0) > 1:
            return [0]*len(nums)
        elif nums.count(0) == 1:
            return [0 if k != 0 else prod for k in nums]
        else:
            return [int(prod/k) for k in nums]
        
        
        
        
        
        
        

        
# #without division ( running left product running right product)
#         l = len(nums)
#         l_prod = [1]*l
#         r_prod = [1]*l
        
#         for i in range(1,len(nums)):
#             l_prod[i] = nums[i-1]*l_prod[i-1]

#         for k in range(-2,-len(nums)-1,-1):
#             r_prod[k] = nums[k+1]*r_prod[k+1]
            
            
#         return [l_prod[i]*r_prod[i] for i in range(len(nums))]
            
            
            
            

        
#With division

#         product = 1
        
#         for i in nums:
#             if i != 0:
#                 product = product*i
#             else:
#                 product = product*1
                

            
#         if 0 in nums:
#             if nums.count(0) > 1:
#                 return [0*i for i in nums]
#             else:
#                 return [0 if p!=0 else product for p in nums]
            
#         #with division   
#         else:
#             return [int(product/k) for k in nums]
        

        
        
                
        

        



            

        
       
        