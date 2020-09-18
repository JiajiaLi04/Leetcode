##  153. Find Minimum in Rotated Sorted Array

## Binary search
class Solution:
    def minArray(self, numbers):
        i=0
        j = len(numbers)-1
        while i<j:
            m = (i+j)//2
            if numbers[m]<numbers[j]:
                j = m
            elif numbers[m] == numbers[j]:
                j = j-1
            else: i = m+1
        return numbers[i]

            
            
        

if __name__ == '__main__':
    func = Solution()
    numbers = [3,4,5,1,2]
    output = func.minArray(numbers)
    print(output)