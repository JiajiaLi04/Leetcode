class Solution:
    def isPalindrome(self, s: str) -> bool:
        for ch in s:
            if ch.isalnum():
                sgood = "".join(ch.lower())
        # sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1] ## [::-1] to do the reverse for tuples, arrays, and strings


if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    s = "A man, a plan, a canal: Panam"
    func = Solution()
    output = func.isPalindrome(s)
    print(output)




