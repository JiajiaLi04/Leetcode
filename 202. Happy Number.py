# ## with the help of Hashset
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         cycle_members = set()
#         while (n!=1):
#             digit =  [int(d) for d in str(n)]
#             temp_n = 0
#             for i in range(len(digit)):
                
#                 temp_n = digit[i]**2 +temp_n
#             n = temp_n
#             if n!=1 and (n in cycle_members):
#                 return False
#                 break           
#             cycle_members.add(n)
     
#         return True


# two pinters. one is slow and another is fast. These two pointers will meet if it is unhappy number
# 慢速在链表中前进 1 个节点，快跑者前进 2 个节点（对 getNext(n) 函数的嵌套调用）。
class Solution:
    def isHappy(self, n: int) -> bool:  
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1
    
        
        
if __name__ == '__main__':
    # n = 19
    n = 116
    func = Solution()
    print(func.isHappy(n))