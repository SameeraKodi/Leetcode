class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        lst = []
        

                
        for j in range(n):
            sublist = []
            for i in range(-1,-n-1,-1):
                
                sublist.append(matrix[i][j])
            lst.append(sublist)
                
            
        
        matrix[::] = lst
        return matrix
        
                
                
                
        