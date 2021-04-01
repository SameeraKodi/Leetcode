class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i,value in enumerate(nums):
            x = target-value
            if x in nums and i != nums.index(x):
                lst.append(i)
                lst.append(nums.index(x))
                break
            else:
                           continue
                           
        return lst
                
                
            
        