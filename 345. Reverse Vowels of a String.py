class Solution:
    def reverseVowels(self, s: str) -> str:
        # a e i o u                                         #元音元素
        # dic = {'a','e','i','o','u','A','E','I','O','U'}     #大小写元音元素集合作为判断依据
        dic = ['a','e','i','o','u','A','E','I','O','U'] 
        pol = 0                                             #左指针
        por = len(s)-1                                      #右指针
        s_ = list(s)                                        #str类型，转换为list, 方便修改数据，因为在python中，str类型是不可变的,
                                                            # 'str' object does not support item assignment
        while pol < por:                                    #左右指针交错循环停止
            if s_[pol] in dic and s_[por] in dic:           #左右指针所指元素均在集合中
                s_[pol], s_[por] = s_[por], s_[pol]         #交换左右指针所指元素
                por -= 1                                    #右指针左移
                pol += 1                                    #左指针右移
            if s_[por] not in dic:                          #右指针所指元素不在集合中
                por -= 1                                    #右指针左移
            if s_[pol] not in dic:                          #左指针所指元素不在集合中
                pol += 1                                    #左指针右移
        return ''.join(s_)   



if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    s = "apple"
    func = Solution()
    output = func.reverseVowels(s)
    print(output)


