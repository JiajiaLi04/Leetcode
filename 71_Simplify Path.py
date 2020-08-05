# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         stack = []
#         path = path.split("/")

#         for item in path:
#             if item == "..":
#                 if stack : 
#                     stack.pop()
#             elif item and item != ".":
#                 stack.append(item)
#         return "/" + "/".join(stack)

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.strip("/").split("/")
        stack = []
        for i in path:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == '':
                pass
            else:
                stack.append(i)
        return   "/" + "/".join(stack)


if __name__ == '__main__':
    func = Solution()
    path = "../home//jia/../hello/"
    path = "/a/./b/../../c/"
    print(func.simplifyPath(path))
