## two pointers
class Solution:
    def removeDuplicates(self, nums):
        if len(nums)==0: 
            return 0
        i =0
        for j in range(len(nums)):
            if nums[j]!=nums[i]:
                i = i+1
                nums[i]=nums[j]
        return i+1

if __name__ == '__main__':
	nums = [0,0,1,1,1,2,2,3,3,4]
	func = Solution()
	print(func.removeDuplicates(nums))