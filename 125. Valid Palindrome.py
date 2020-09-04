class Solution:
    def isPalindrome(self, s: str) -> bool:
        for ch in s:
            if ch.isalnum():
                A = ch.lower()
        sgood = "".join(A)
        # sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    func = Solution()
    output = func.isPalindrome(s)
    print(output)




