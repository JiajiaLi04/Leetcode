class Solution:
    def trap(self, heights):
        n = len(heights)
        l, r = [0] * (n + 1), [0] * (n + 1)
        ans = 0
        for i in range(1, len(heights) + 1):
            l[i] = max(l[i - 1], heights[i - 1])
        for i in range(len(heights) - 1, 0, -1):
            r[i] = max(r[i + 1], heights[i])
        for i in range(len(heights)):
            ans += max(0, min(l[i + 1], r[i]) - heights[i])
        return ans 



if __name__ == '__main__':
    func = Solution()
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(func.trap(heights))
    
    