class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        curr_length = 0
        max_length = 0
        str_set = set() ## hashset
        for i in range(len(s)):
            while s[i] in str_set:           
                str_set.remove(s[left])
                left = left+1
            str_set.add(s[i])
            curr_length = i - left + 1
            max_length = max(max_length, curr_length)
        return max_length
            
## solution from others
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s:return 0
#         left = 0
#         # 哈希集合，记录每个字符是否出现过
#         lookup = set()
#         n = len(s)
#         max_len = 0
#         cur_len = 0
#         for i in range(n):
#             cur_len += 1
#             ## check whether current element is in hashset.
#             while s[i] in lookup:
#                 lookup.remove(s[left])
#                 left += 1
#                 cur_len -= 1
#             if cur_len > max_len:max_len = cur_len
#             lookup.add(s[i])
#         return max_len



        
if __name__ == '__main__':
    func = Solution()
    s = 'pwwkew'
    print(func.lengthOfLongestSubstring(s))