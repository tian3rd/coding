#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 0


    def push(self, x: int) -> None:
        self.stack.append(x)
        sorted_stack = sorted(self.stack)
        self.min = sorted_stack[0]
        

    def pop(self) -> None:
        if self.stack == []:
            return None
        self.stack.pop()
        if self.stack == []:
            self.min = None
        else:
            sorted_stack = sorted(self.stack)
            self.min = sorted_stack[0]
        

    def top(self) -> int:
        if self.stack == []:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

