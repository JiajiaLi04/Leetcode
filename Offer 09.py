class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)


    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


# class CQueue:
#     def __init__(self):
#         self.A, self.B = [], []

#     def appendTail(self, value: int) -> None:
#         self.A.append(value)

#     def deleteHead(self) -> int:
#         if self.B: return self.B.pop()
#         if not self.A: return -1
#         while self.A:
#             self.B.append(self.A.pop())
#         return self.B.pop()



if __name__ == '__main__':
    obj = CQueue()
    value = 3
    obj.appendTail(value)
    param_2 = obj.deleteHead()
    print("it is done")

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()