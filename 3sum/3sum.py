class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        lst = []
        for i in range(len(nums[:-2])):

            if (i == 0) or (nums[i] != nums[i-1]):
                target = 0-nums[i]
                low_p = i+1
                high_p = len(nums) - 1
                
                while low_p < high_p:
                    s = nums[low_p] + nums[high_p]
                    if s == target:
                        lst.append([nums[i],nums[low_p],nums[high_p]])
    
                        while low_p < high_p and nums[low_p] == nums[low_p+1]:
                            low_p += 1
                        while low_p < high_p and nums[high_p] == nums[high_p-1]:
                            high_p -= 1
                        low_p += 1
                        high_p -= 1
        
                    elif s < target:
                        low_p += 1
                        
                    else:
                        high_p -= 1
        return lst
                        
                
                