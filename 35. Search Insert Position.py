class Solution:
    def searchInsert(self, nums, target):
        h = []
        for i, value in enumerate(nums):
            if target==value:
                return i
            elif (target>):
                h.append(value)
                return(nums.index(target))
                

if __name__ == '__main__':
    func = Solution()
    nums = [1,3,5,6]
    target = 5
    print(func.searchInsert(nums, target))

