## sort it firstly
class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            ##  nums1[i] != ans[-1] avoid repeating ans.
            if nums1[i] == nums2[j] and (not ans or nums1[i] != ans[-1]):
                ans.append(nums1[i])
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans

# ## Using hash set
# ## time complexity: O(n×m). Space complexicity O(1)
# class Solution:
#     def set_intersection(self, set1, set2):
#         for x in set1:
#             if x in set2:
#                 return x
            
#         # return [x for x in set1 if x in set2]
        
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """  
#         set1 = set(nums1)
#         set2 = set(nums2)
        
#         if len(set1) < len(set2):
#             return self.set_intersection(set1, set2)
#         else:
#             return self.set_intersection(set2, set1)


if __name__ == '__main__':
    func = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(func.intersection(nums1, nums2))
    

