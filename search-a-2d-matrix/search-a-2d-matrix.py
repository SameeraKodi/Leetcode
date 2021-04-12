class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        #check which row it falls in for that get the starting values of all rows
        lst_starts = [item[0] for item in matrix]

        
        if target >= lst_starts[-1]:
            return True if target in matrix[-1] else False
        elif target <= lst_starts[0]:
            return True if target in matrix[0] else False
        else:
            lst = []

            for i in range(len(lst_starts)-1):
                print(lst_starts[i],lst_starts[i+1])
                if target >= lst_starts[i]  and target < lst_starts[i+1]:
                    lst.append(1)
                else:
                    lst.append(0)
     

        idx = lst.index(1)
        return True if target in matrix[idx] else False
                    
                    
            
        # else:
        #     idx = self.binarysearch(lst_starts,target)
        #     print("idx",idx)
        
        
        
    # def binarysearch(self,nums:list,target:int) -> int:
    #     #return the index of nums after which target comes
    #     l = 0
    #     r = len(nums) -1
    #     if target < nums[l] or target>nums[r]:
    #         return False
    #     while l <= r:
    #         print(l,r)
    #         mid = (l+r)//2
    #         print('mid',mid)
    #         if target == nums[mid]:
    #             return mid
    #         elif target > nums[mid]:
    #             l = mid + 1
    #         else:
    #             r = mid -1
    #     return l-1
    
    
    #binary with ending elements
    
    
        


 
        