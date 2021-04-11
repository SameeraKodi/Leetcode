class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        result = []
        
        for i in range(1,len(prices)):
            buy_price = prices[i-1]
            if prices[i] > buy_price:
                profit = max(profit,prices[i]-buy_price)
                result.append(profit)
                profit = 0
            else:
                buy_price = prices[i]
        
        return sum(result)
        
        
        
        
        
        
        
        
        
        
#        #since multiple transactions are allowed we have to keep track of all possible profits hence the final list
#         profit = 0
#         final = []
        
#         for i in range(1,len(prices)):
#             buy_price = prices[i-1]
#             if prices[i] > buy_price: #this is condition implying selling
#                 profit = max(profit,prices[i]- buy_price)
#                 final.append(profit)
#                 profit = 0


#             else: #this is condition implying no sale so change in buy price
#                 buy_price = prices[i]
                
#         return sum(final)