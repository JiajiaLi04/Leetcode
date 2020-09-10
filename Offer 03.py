# class Solution:
#     # 利用Python中的Hash set集合为无序不重复集合
#     def findRepeatNumber(self, nums: [int]) -> int:
#         dic = set()
#         for num in nums:
#             if num in dic:
#                 return num
#             else:
#                 dic.add(num)
#         return -1

'''
方法二：原地交换
题目说明尚未被充分使用，即 在一个长度为 n 的数组 nums 里的所有数字都在 0 ~ n-1 的范围内 。 此说明含义：数组元素的 索引 和 值 是 一对多 的关系。
因此，可遍历数组并通过交换操作，使元素的 索引 与 值 一一对应（即 nums[i] = i）。因而，就能通过索引映射对应的值，起到与字典等价的作用。。
遍历中，第一次遇到数字 x 时，将其交换至索引 x 处；而当第二次遇到数字 x 时，一定有 nums[x] = x，此时即可得到一组重复数字。

算法流程：
遍历数组 nums ，设索引初始值为 i = 0:

若 nums[i] = i： 说明此数字已在对应索引位置，无需交换，因此跳过；
若 nums[nums[i]] = nums[i] ： 代表索引 nums[i]nums[i] 处和索引 ii 处的元素值都为 nums[i] ，即找到一组重复值，返回此值 nums[i]；
否则： 交换索引为 i 和 nums[i] 的元素值，将此数字交换至对应索引位置。
若遍历完毕尚未返回，则返回 −1 。

复杂度分析：
时间复杂度 O(N) ： 遍历数组使用 O(N) ，每轮遍历的判断和交换操作使用 O(1) 。
空间复杂度 O(1) ： 使用常数复杂度的额外空间。

'''



class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: 
                return nums[i]
            else:
                # Python 中， a,b=c,d 操作的原理是先暂存元组 (c, d)，然后 “按左右顺序” 赋值给 a 和 b 。
                # swap nums[i] and nums[nums[i]]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1



if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    nums = [2, 3, 1, 0, 2, 5, 3]
    func = Solution()
    output = func.findRepeatNumber(nums)
    print(output)

