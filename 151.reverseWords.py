class Solution:
    def reverseWords(self, s: str) -> str:
        output = s.split()
        rev_output = output.reverse()
        return " ".join(output)
        

        


if __name__ == '__main__':
    func = Solution()
    # s = "the sky is blue"
    s = " hello world!  "
    print(func.reverseWords(s))
