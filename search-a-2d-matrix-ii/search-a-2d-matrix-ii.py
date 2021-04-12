class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        row_ptr = 0
        col_ptr = len(matrix[0])-1
        
        while row_ptr < len(matrix) and col_ptr >= 0:
            if target < matrix[row_ptr][col_ptr]:
                col_ptr -= 1
            elif target > matrix[row_ptr][col_ptr]:
                row_ptr += 1
            else:
                return True
            
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return False
        
#         row = 0
#         col = len(matrix[0]) - 1
        
#         while row < len(matrix) and col >= 0:
#             if matrix[row][col] == target:
#                 return True
#             elif matrix[row][col] > target:
#                 col -= 1
#             else:
#                 row += 1
                
#         return False
        
        
        

                
            
        