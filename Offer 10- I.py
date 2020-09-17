     
# class Solution:
#     def fib(self, n: int) -> int:
#         a, b = 0, 1
#         for _ in range(n):
#             a, b = b, a + b
#         return a % 1000000007

class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        
        dp = [None] * (n+1)
        dp[0]=0
        dp[1]=1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= 1000000007
        return dp[i]
        

if __name__ == '__main__':
    func = Solution()
    n = 0
    output = func.fib(n)
    print(output)