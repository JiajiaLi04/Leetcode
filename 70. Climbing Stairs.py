class Solution:
    def climbStairs(self, n: int) -> int:
        p = 0
        q = 0
        r = 1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r
    
if __name__ == '__main__':
    n = 3
    func = Solution()
    output = func.climbStairs(n)
    print(output)
