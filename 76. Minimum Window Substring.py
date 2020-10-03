class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ''
        left_index = 0
        index_record = []
        min_length = 10e9
        counter = 0

        for i in range(len(s)):
            curr_string = s[left_index:i+1]
            
            for i in range(len(t)):
                if t[i] not in curr_string:
                    counter= counter+1
            if counter==0:
            
            # while set(t).issubset(set(curr_string)):
                if (i-left_index+1)<min_length:
                    min_length = i-left_index+1
                    index_record = [left_index, i]
                if left_index>=len(s)-1:
                    break
                # index_record.append([left_index, i])
                left_index = left_index + 1
                curr_string = s[left_index:i+1]

                if left_index>=len(s)-1:
                    continue
                while s[left_index] not in t:
                    left_index = left_index + 1
                    curr_string = s[left_index:i+1]
        if len(index_record)==0:
            return ''
        else:
            return s[index_record[0]: index_record[1]+1]
        # return ' '


        # if len(index_record):
        #     length_min = []
        #     for i in range(len(index_record)):
        #         length_min.append(index_record[i][1] - index_record[i][0])

        #     index = min(length_min)
        # else:
        #     return ' '
            
                

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if len(t)>len(s):
#             return ' '
#         left_index = 0
#         index_record = []
#         min_length = 10e9
#         for i in range(len(s)):
#             curr_string = s[left_index:i+1]
#             while set(t).issubset(set(curr_string)):
#                 index_record.append([left_index, i])
#                 left_index = left_index + 1
#                 curr_string = s[left_index:i+1]

#                 while s[left_index] not in t:
#                     left_index = left_index + 1
#                     curr_string = s[left_index:i+1]


#         if len(index_record):
#             length_min = []
#             for i in range(len(index_record)):
#                 length_min.append(index_record[i][1] - index_record[i][0])

#             index = min(length_min)
#         else:
#             return ' '
            
                



if __name__ == '__main__':
    func = Solution()
    # S = "ADOBECODEBANC"
    # T = "ABC"
    S = "ab"
    T = "b"
    print(func.minWindow(S, T))