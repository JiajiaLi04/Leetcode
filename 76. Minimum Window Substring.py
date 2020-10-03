class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ' '
        left_index = 0
        # right_index = 0
        curr_index = 0
        for i in range(len(s)):
            curr_index  = len(s) + 1
            if curr_index



        if not s:return 0
        left = 0
        # 哈希集合，记录每个字符是否出现过
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            ## check whether current element is in hashset.
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len


if __name__ == '__main__':
    func = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    print(func.minWindow(S, T))