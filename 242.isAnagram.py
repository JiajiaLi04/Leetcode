class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ds = {}
        dt = {}
        for i in s:
            if i in ds:
                ds[i] = ds[i] + 1
            else:
                ds[i] = 1
        for j in t:
            if j in dt:
                dt[j] = dt[j] + 1
            else:
                dt[j] = 1
        for x in ds:
            if x not in dt or ds[x]!=dt[x]:
                return False
        return True


if __name__ == '__main__':
    func = Solution()
    s = "anagram"
    t = "nagaram"
    print(func.isAnagram(s, t))