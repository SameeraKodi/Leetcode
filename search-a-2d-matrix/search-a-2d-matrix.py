class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        #binary search 
        l = 0
        r = m*n - 1
        while l<=r:
            mid = (l+r)//2
            value_mid = matrix[mid//n][mid%n]
        
            if target == value_mid:
                return True
            elif target > value_mid:
                l = mid+1
            else:
                r = mid-1
        return False
 
        