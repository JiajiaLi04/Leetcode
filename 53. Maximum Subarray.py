## greedy algorithm
# class Solution(object):
#     def maxSubArray(self, nums):
#         if not nums:
#             return -2147483648
#         cur_sum = max_sum=nums[0]
#         for i in range(1, len(nums)):
#             cur_sum = max(nums[i], cur_sum+nums[i])
#             max_sum = max(cur_sum, max_sum)
#         return max_sum

# Dynamic programming
class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i]=nums[i]+nums[i-1]
        return max(nums)
    
if __name__ == '__main__':
    func = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(func.maxSubArray(nums))