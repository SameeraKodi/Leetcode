class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic ={}
        count = 0
        for i in nums:
            if i in dic:
                continue
            else:
                dic[i]  = nums.count(i)
        for k,v in dic.items():
            if v ==1:
                return k
                

                
            
        