import numpy as np
import sys

class Solution:
    def oppo1(self, input):
        output = []
        for i in range(input[0][0]):
            H = input[i+1][0]
            W = input[i+1][1]
            K = input[i+1][2]

            # temp_coord = np.zeros((H*W, 2))
            temp_sum_digits = np.zeros((H*W, 1))
            for i in range(H):
                # temp_coord[i:(i+1)*W, :] = [H, np.array(range(W))]
                temp_sum_digits[i:(i+1)*W, :] = H + np.array(range(W))
            output_temp = sum(temp_sum_digits<=K)
          
            output.append(output_temp)
        return output

if __name__ == '__main__':
    func = Solution()
    input = [[3],[1, 1, 0], [2, 3, 1], [2, 3, 2]]
    print(func.oppo1(input))
