
class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        for i in range(n):
            low, high = i + 1, n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1        
        return [-1, -1]


if __name__ == '__main__':
    func = Solution()
    numbers = [2,7,11,15]
    target = 9
    print(func.twoSum(numbers, target))