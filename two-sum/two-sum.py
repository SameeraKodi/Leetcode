class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i, val in enumerate(nums):
            x = target - val
            if x not in d:
                d[val] = i

            else:
                return([i,d[x]])
         


            
        
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#                 #you have a target, check if value and target - value exist in the lst and make sure they don't have the same index
#         lst = []
#         for i,value in enumerate(nums):
#             x = target-value
#             if x in nums and i != nums.index(x):
#                 lst.append(i)
#                 lst.append(nums.index(x))
#                 break
#             else:
#                            continue
                           
#         return lst

       # # dictionary solution
       #  dic = {}
       #  for i,val in enumerate(nums):
       #      x = target-val
       #      if x not in dic:
       #          dic[val] = i
       #      else : 
       #          return [i,dic[x]]
        
        
        
        

 
            

            
                
        