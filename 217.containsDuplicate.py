class Solution:
    def containsDuplicate(self, nums) -> bool:
        # 声明集合
        s = set()
        # 遍历数组，将元素添加到集合中
        for num in nums:
            # 若元素存在于集合中，表示存在重复元素
            if num in s:
                return True
            s.add(num)
        return False


if __name__ == '__main__':
    func = Solution()
    nums = [1,2,3,1]
    print(func.containsDuplicate(nums))

