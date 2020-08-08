class Solution(object):
    # Brute force
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans



if __name__ == '__main__':
    func = Solution()
    # heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    n = 3
    print(func.generateParenthesis(n))