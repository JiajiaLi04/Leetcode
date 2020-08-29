class Solution:
    def intersect(self, nums1, nums2):
        
        ## sort it firstly
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i +=1
                j +=1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans

# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1.sort()
#         nums2.sort()

#         length1, length2 = len(nums1), len(nums2)
#         intersection = list()
#         index1 = index2 = 0
#         while index1 < length1 and index2 < length2:
#             if nums1[index1] < nums2[index2]:
#                 index1 += 1
#             elif nums1[index1] > nums2[index2]:
#                 index2 += 1
#             else:
#                 intersection.append(nums1[index1])
#                 index1 += 1
#                 index2 += 1
        
#         return intersection

if __name__ == '__main__':
    func = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(func.intersect(nums1, nums2))