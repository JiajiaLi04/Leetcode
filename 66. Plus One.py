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
    nums = [9,0,9,9,9]
    print(func.plusOne(nums))
        