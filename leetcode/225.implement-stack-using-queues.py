#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
import queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.q1.qsize() == 0 and self.q2.qsize() == 0:
            self.q1.put(x)
        else:
            if self.q1.qsize() != 0:
                self.q1.put(x)
            else:
                self.q2.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1.qsize() != 0:
            while self.q1.qsize() != 1:
                self.q2.put(self.q1.get())
            return self.q1.get()
        elif self.q2.qsize() != 0:
            while self.q2.qsize() != 1:
                self.q1.put(self.q2.get())
            return self.q2.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        rtn = self.pop()
        self.push(rtn)
        return rtn

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.q1.qsize() != 0 or self.q2.qsize() != 0:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

