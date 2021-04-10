class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lst = []
        
        rowstart = 0
        rowend = len(matrix) - 1 
        colstart = 0
        colend = len(matrix[0]) - 1
        
        while rowstart <= rowend and colstart <= colend:
            print("1")
            for i in range(colstart,colend+1):
                lst.append(matrix[rowstart][i])
            rowstart += 1
            print('2')
            for i in range(rowstart,rowend+1):
                lst.append(matrix[i][colend])
            colend -= 1
            print('3')
            if rowstart <= rowend:
                for i in range(colend,colstart-1,-1):
                    lst.append(matrix[rowend][i])
                rowend -= 1
                    
            if colstart <= colend:
                for i in range(rowend,rowstart-1,-1):
                    lst.append(matrix[i][colstart])
                colstart += 1
                    
        return lst
                
        