class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                ans = max(ans, prices[i] - minimum)

        return ans