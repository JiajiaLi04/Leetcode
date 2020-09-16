# class Solution:
#     def isPalindrome(self, s: str) -> bool:     
#         sgood = ''
#         for ch in s:
#             if ch.isalnum(): # The isalnum() method checks whether the string consists of alphanumeric characters.
#                 sgood = sgood + "".join(ch.lower())
#         ## the above can be substitued using the following one line        
#         # sgood = "".join(ch.lower() for ch in s if ch.isalnum())
#         return sgood == sgood[::-1] ## [::-1] to do the reverse for tuples, arrays, and strings

# ## two pointers
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         sgood = "".join(ch.lower() for ch in s if ch.isalnum())
#         n = len(sgood)
#         left, right = 0, n - 1
        
#         while left < right:
#             if sgood[left] != sgood[right]:
#                 return False
#             left, right = left + 1, right - 1
#         return True


## two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        
        # The isalnum() method checks whether the string consists of alphanumeric characters.
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1

        return True

if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    s = "A man, a plan, a canal: Panam"
    func = Solution()
    output = func.isPalindrome(s)
    print(output)




