## Recursive
# class Solution:
#     def reverseString(self, s):
#         def helper(left, right):
#             if left < right:
#                 s[left], s[right] = s[right], s[left]
#                 helper(left + 1, right - 1)

#         helper(0, len(s) - 1)


## Two pointers
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1



if __name__ == '__main__':
	s = ["h","e","l","l","o"]
	func = Solution()
	func.reverseString(s)
	print(s)
