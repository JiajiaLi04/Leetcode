class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums) -1

        while left<=right:
            # middle = left + (right-left)//2
            middle  = (left + right) // 2
            if nums[middle]==target:
                return middle
            if nums[middle]>= nums[left]:
                if nums[left]<=target<=nums[middle]:
                    right = middle-1
                else:
                    left = middle +1
            if nums[middle]<=nums[right]:
                if nums[middle]<=target<=nums[right]:
                    left = middle +1
                else:
                    right = middle -1
        return -1


if __name__ == '__main__':
    func = Solution()
    nums = [1,3]
    target = 3
    output = func.search(nums, target)
    print(output)       