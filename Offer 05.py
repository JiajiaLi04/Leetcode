# class Solution:
#     def replaceSpace(self, s: str) -> str:
#         s_list = list(s)
#         for i in range(len(s_list)):
#             if s[i]==' ':
#                 s_list[i] = '%20'
#         return ''.join(s_list) 

               
# class Solution:
#     def replaceSpace(self, s: str) -> str:
#         new_s = ''
#         for i in range(len(s)):
#             if s[i]==' ':
#                 new_s = new_s + '%20'
#             else:
#                 new_s = new_s + s[i]
#         return new_s

class Solution:
    def replaceSpace(self, s: str) -> str:
        lst = s.split(' ')
        return '%20'.join(lst)                  


if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    s = "We are happy."
    func = Solution()
    output = func.replaceSpace(s)
    print(output)

