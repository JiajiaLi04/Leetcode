class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        for i in range(m):
            for j in range(n):
                sums = i%10 + 


if __name__ == '__main__':
    func = Solution()
    m = 2
    n = 3
    k = 1
    output = func.movingCount(m, n, k)
    print(output)