class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        count = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                
                if grid[i][j] == "0":
                    continue
                else:
                    count += 1
                    stack = list()
                    stack.append([i,j])
                    
                    while len(stack) != 0:
                        
                        [p,q] = stack.pop()
                        
                        #up
                        if p >= 1 and grid[p-1][q] == "1":
                            stack.append([p-1,q])
                        
                        #down
                        if p < row-1 and grid[p+1][q] == "1":
                            stack.append([p+1,q])
                            
                        #left
                        if q >= 1 and grid[p][q-1] == "1":
                            stack.append([p,q-1])
                            
                        #up
                        if q< col-1  and grid[p][q+1] == "1":
                            stack.append([p,q+1])
                            
                        grid[p][q] = "0"

        return count
                            
        
        
        
                        
                