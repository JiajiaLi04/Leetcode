class Solution:
    def uniqueAward(self , nums ):
        # write code here
        i = 0
        temp = 0
        if len(nums)==0:
            return None
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                temp = temp+1
            if temp==(len(nums)-1):
                return nums[i]


if __name__ == '__main__':
    nums = [3]
    func = Solution()
    print(func.uniqueAward(nums))