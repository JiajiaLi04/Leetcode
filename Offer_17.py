class Solution:
    def printNumbers(self, n: int):
        output = list(range(1, 10**n))
        return output
        
        
        
        
if __name__ == '__main__':
    n = 2
    func = Solution()
    output = func.printNumbers(n)
    print(output)
