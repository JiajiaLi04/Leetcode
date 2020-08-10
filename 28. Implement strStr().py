# class Solution:
#     def strStr(self, haystack, needle):
#         if len(needle)==0:
#             return 0
        
#         for i in range(len(haystack)):
#             if needle[0]==haystack[i]:
#                 if needle==haystack[i:i+len(needle)]:
#                     return i
#         return -1
        


class Solution:
    def strStr(self, haystack, needle):
        if (needle==''):
            return 0            
        elif (len(haystack)-len(needle)<0) | (haystack==''):
            return -1
        else:
            i = 0
        for i in range(len(haystack)):
            if needle[0]==haystack[i]:
                if needle==haystack[i:i+len(needle)]:
                    return i
            elif (i+len(needle))<=len(haystack):
                i = i+len(needle)
        return -1
        
        
if __name__ == '__main__':
    func = Solution()
    haystack = 'hello'
    needle = 'lo'
    print(func.strStr(haystack, needle))

