class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dynamicProg=[math.inf] * (amount+1)
        dynamicProg[0]=0
        
        for coin in coins:
            for i in range(coin, amount+1):
                if i-coin>=0:
                    dynamicProg[i]=min(dynamicProg[i], dynamicProg[i-coin]+1)
        
        return -1 if dynamicProg[-1]==math.inf else dynamicProg[-1]
                