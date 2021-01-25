class Solution:
    def missingNumber(self, nums):
        s = set()
        for num in nums:
            s.add(num)
        output = []
        for i in range(len(nums)+1):
            if i not in s:
                output.append(i)
        return output[0]

if __name__ == '__main__':
    func = Solution()
    nums = [3,0,1]
    print(func.missingNumber(nums))

        