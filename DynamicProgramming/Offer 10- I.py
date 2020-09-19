# dynamic programming
class Solution:
    def fib(self, n: int) -> int:
        sum = [None] * (n+1)
        if n==0:
            return 0
        sum[0]=0
        sum[1]=1        
        for i in range(2,n+1):
            sum[i] = sum[i-1] + sum[i-2]
        return sum[n] % 1000000007

'''
a, b = b, a + b
When dealing with expressions in python, everything to the right of the ‘=’ operator, i.e. the assignment operator, is evaluated 
first then assigned to the variables to the left.
'''
## 由于只用到前面两个状态，可以进一步优化
# # dynamic programming
# class Solution:
#     def fib(self, n: int) -> int:
#         a, b = 0, 1
#         for _ in range(n):
#             sum = a + b
#             a = b
#             b = sum

#             # a, b = b, a + b
#         return a % 1000000007



# ## recursive 
# # 费时间，leetcode超出时间限制   
# class Solution:
#     def fib(self, n: int):
#         def fib_output(n):

#             if n==0:
#                 return 0
#             if n==1:
#                 return 1
#             else:
#                 return fib_output(n-1)+fib_output(n-2)
#         return fib_output(n)


if __name__ == '__main__':
    func = Solution()
    n =0
    output = func.fib(n)
    print(output)