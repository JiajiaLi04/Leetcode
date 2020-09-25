class Solution:
    def hammingWeight(self, n: int) -> int:
    # 与运算 & 和位移 >>=
        ans = 0
        while n > 0:
            ## n & 1 to know whether the current digit is 1.
            ans += n & 1
            n = n>> 1 # n >>= 1
        return ans

        
if __name__ == '__main__':
    ## the way to show binary numbers in python
    n = 0b00000000000000000000000000001011
    func = Solution()
    output = func.hammingWeight(n)
    print(output)
