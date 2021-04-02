class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        final = []
        
        for i in range(1,len(prices)):
            buy_price = prices[i-1]
            if prices[i] > buy_price:
                #print(prices[i],buy_price)
                profit = max(profit,prices[i]- buy_price)
                #print(profit)
                final.append(profit)
                profit = 0
                #print(final)

                
            else:
                buy_price = prices[i]
                
        return sum(final)


                
                
            
        