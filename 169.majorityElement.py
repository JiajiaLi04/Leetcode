class Solution:
    def majorityElement(self, nums) -> int:
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        print(nums_count.values())
        print('hello')

        # dct = defaultdict(int)
        # for i in nums:
        #     dct[i] += 1

        # return max(nums_count.keys(), key=lambda x: nums_count[x])
        # return max(nums_count, key=nums_count.get)
        return max(nums_count.keys(), key=nums_count.get)



if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    func = Solution()
    output = func.majorityElement(nums)
    print(output)
