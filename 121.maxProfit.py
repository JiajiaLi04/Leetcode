# class Solution:
#     def maxProfit(self, prices) -> int:
#         i = 0
#         j = i+1
#         max_value = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 temp = prices[j] - prices[i]
#                 max_value  = max(temp, max_value)
#         return max_value

class Solution:
    def maxProfit(self, prices) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    func = Solution()
    output = func.maxProfit(prices)
    print(output)
