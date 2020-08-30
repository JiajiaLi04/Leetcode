class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans


if __name__ == '__main__':
    func = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(func.maxArea(height))
