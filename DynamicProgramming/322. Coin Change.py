# ## Dynamic programming
# ## the method of recursive
# # leetcode超出时间限制
# class Solution:
#     def coinChange(self, coins, amount: int) -> int:
#         def dp(amount):
#             if amount==0:
#                 return 0
#             if amount<0:
#                 return -1
#             res= float("inf")
#             for i in range(len(coins)):
#                 subproblem = dp(amount-coins[i])
#                 if subproblem==-1:
#                     continue
#                 res = min(res, 1 + subproblem)
#             if res!= float("inf"):
#                 return res
#             else:
#                 return -1
#         return dp(amount)

# class Solution:
#     def coinChange(self, coins, amount: int) -> int:
#         dp = [0]*(amount+1)
#         for i in range(1, amount+1):
#             dp[i] = 1e8
#             for coin in coins:
#                 if i >= coin and dp[i-coin] != 1e8:
#                     dp[i] = min(dp[i], dp[i-coin]+1)
#         if dp[-1] == 1e8:
#             return -1
#         else:
#             return dp[-1]


# ## 添加备忘录记录每一步的值
# class Solution:
#     def coinChange(self, coins, amount: int) -> int:
#         mem = dict()
#         def dp(n):
#             for n in mem:
#                 return mem[n]
#             if n==0:
#                 return 0
#             if n<0:
#                 return -1
#             res= float("inf")
#             for i in range(len(coins)):
#                 subproblem = dp(n-coins[i])
#                 if subproblem==-1:
#                     continue
#                 res = min(res, 1 + subproblem)
#             if res!= float("inf"):
#                 mem[n] = res
#             else:
#                 mem[n] =  -1
#             return mem[n]
#         return dp(amount)

class Solution:
    def coinChange(self, coins, amount: int):
        # 备忘录
        memo = dict()
        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)

if __name__ == '__main__':
    func = Solution()
    coins = [1, 2, 5]
    amount = 11
    # coins = [2]
    # amount = 3
    output = func.coinChange(coins, amount)
    print(output)