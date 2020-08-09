# class Solution:
#     # def twoSum(self, nums: List[int], target: int) -> List[int]:
#     def twoSum(self, nums, target):
    
#     #:type nums: List[int]
#     #:type target: int
#     #:rtype: List[int]
#     ## using hash table
#         h = {}
#         for i, num in enumerate(nums):
#             n = target - num
#             if n not in h:
#                 h[num] = i
#             else:
#                 return [h[n], i]  

class Solution:
    ## sorting and two pointers
    def twoSum(self, nums, target):
        temp=nums.copy()
        temp.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if (temp[i]+temp[j])>target:
                j=j-1
            elif (temp[i]+temp[j])<target:
                i=i+1
            else:
                break
        p=nums.index(temp[i])
        # nums.pop(p)
        k=nums.index(temp[j])
        # if k>=p:
        #     k=k+1
        return [p,k]



if __name__ == '__main__':
    func = Solution()
    nums = [2, 11,6, 7, 15,4]
    target = 9
    print(func.twoSum(nums, target))

