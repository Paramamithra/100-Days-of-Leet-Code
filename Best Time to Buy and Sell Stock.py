class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=prices[0] #assume first day price is lowest price
        max=0 #let maximum profit be zero
        for price in prices: #loop through each day
            if price>low: #if days price is greater than lowest price
                if max<price-low:#check if selling on the day can get maximum profit
                    max=price-low#if yes change maximum profit
            else:
                low=price #if days price is lesser than lowest price change lowest price
        return max
