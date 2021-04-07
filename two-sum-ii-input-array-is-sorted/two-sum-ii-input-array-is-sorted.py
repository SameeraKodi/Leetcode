class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_1 = 0
        pointer_2 = len(numbers) - 1
        
        while pointer_1 <= pointer_2:
            sum = numbers[pointer_1] + numbers[pointer_2]
            if sum == target:
                return [pointer_1+1,pointer_2+1]
            elif sum < target:
                pointer_1 += 1
            else:
                pointer_2 -= 1
                
        return [pointer_1+2,pointer_2+1]
                
            
        