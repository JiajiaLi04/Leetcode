# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         if not a or not b:  ##check a, b blank or not
#             return a or b
#         '''
#         [::-1] could reverse the string
#         the slice statement [::-1] means start at the end of the string and end at position 0, 
#         move with the step -1, negative one, which means one step backwards.
#         '''
#         a, b, ans = a[::-1], b[::-1], []
#         # carry: 进位
#         i = j = carry = 0   
#         while i < len(a) or j < len(b) or carry:
#             if i < len(a):
#                 n1 = int(a[i]) 
#             else: 
#                 n1 = 0
#             if j < len(b):
#                  n2 = int(b[j])
#             else: 
#                 n2 = 0
            
#             # n1 = int(a[i]) if i < len(a) else 0
#             # n2 = int(b[j]) if j < len(b) else 0
#             carry, cur = divmod(n1 + n2 + carry, 2) #divmod is very useful
#             ans.append(str(cur))
#             i, j = i + 1, j + 1
#         return ''.join(ans[::-1])


class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2) ## convert to int number.
        while y:
            answer = x ^ y
            ## "<<"" Zero fill left shift, Shift left by pushing zeros in from the right and let the leftmost bits fall off
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    func = Solution()
    output = func.addBinary(a, b)
    print(output)















