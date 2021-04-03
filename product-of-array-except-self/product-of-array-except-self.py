class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        for i in nums:
            if i != 0:
                product = product*i
            else:
                product = product*1
                

            
        if 0 in nums:
            if nums.count(0) > 1:
                return [0*i for i in nums]
            else:
                return [0 if p!=0 else product for p in nums]
            
            
        else:
            return (int(product/k) for k in nums)
                
        

        



            

        
       
        