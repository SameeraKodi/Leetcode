class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #keep the initital buy price as the first day
        buy_price = prices[0]
        #initial profit as 0 ( works well for monotonically decreasing case)
        profit = 0
        
        #now loop through the list ( only once) to update the buy price and profit as we go along
        for i in range(1,len(prices)):
            if prices[i] > buy_price:
                profit = max(profit, prices[i]-buy_price)
                
            #to save the lowest buy_price
            else:
                buy_price = prices[i]
                
                
        return profit
                
                
            
            
            

                
        
        
        