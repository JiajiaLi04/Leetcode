# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         i = len(digits)-1
#         if i>0:
#             digits[i] +=1
#             digits[i] = digits[i]%10
#             if digits[i]!=0:
#                 return digits
#             i = i-1

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i]<9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits
 
if __name__ == '__main__':
    func = Solution()
    nums = [9,0,9,0,9]
    print(func.plusOne(nums))
        