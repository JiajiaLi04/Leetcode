class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==target:
                    return True
                else:
                    return False


if __name__ == '__main__':
    func = Solution()
    
    matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]
    
    target = 5

    print(func.findNumberIn2DArray(matrix, target))
