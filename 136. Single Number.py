class Solution:
    def singleNumber(self, nums) -> int:
        r = 0
        for i in nums:
            r ^= i
        return r


if __name__ == '__main__':
    func = Solution()
    nums = [9,1,9,2,2]
    print(func.singleNumber(nums))
