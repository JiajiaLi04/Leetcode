## Binary search
class Solution:
    def findMin(self, nums) -> int:
        left = 0
        right = len(nums)-1

        while left<right:
            middle = (right+left)//2
            if nums[middle]>nums[right]:
                left = middle +1
            elif nums[middle]<nums[right]:
                right = middle
            else: 
                right = right - 1
        return nums[right]


if __name__ == '__main__':
    func = Solution()
    # numbers = [3,4,5,1,2]
    # nums = [2,2,2,0,1]
    nums = [1, 3, 5]

    output = func.findMin(nums)
    print(output)