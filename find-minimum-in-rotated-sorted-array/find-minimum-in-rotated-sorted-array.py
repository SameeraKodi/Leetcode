class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right)//2
            print(nums[mid])
            
            if nums[mid] >= nums[right]:
                left = mid + 1
                print(left)
            else:
                right = mid
                print(right)
                
        return nums[left]
                
        