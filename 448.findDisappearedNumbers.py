# class Solution:
#     def findDisappearedNumbers(self, nums):
#         # 声明集合
#         s = set()
#         output = []
#         # 遍历数组，将元素添加到集合中
#         for num in nums:
#             s.add(num)
#         for i in range(len(nums)):
#             if (i+1) not in s:
#                 output.append((i+1))
#         return output

class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index]>0:
                nums[index] *= -1
        output = []
        for i in range(len(nums)):
            if nums[i]>0:
                output.append((i+1))
        return output

if __name__ == '__main__':
    func = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(func.findDisappearedNumbers(nums))