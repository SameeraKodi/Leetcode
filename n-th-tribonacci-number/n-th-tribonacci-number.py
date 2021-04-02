class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0,1,1]

        for i in range((n+1)-3):
            #s = T[i] + T[i+1] + T[i+2]
            s = sum(T[i:i+3])
            T.append(s)
        return T[n]
            

            
        
        