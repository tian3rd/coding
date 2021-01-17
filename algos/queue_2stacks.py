'''
Using two stacks to implement a queue. 
'''
import unittest

class Queue2Stack: 
    def __init__(self): 
        self.in_stack = []
        self.out_stack = []
    
    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self, item):
        self.in_stack.append(item)

    def pop(self): 
        if not self.out_stack:
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()

class TestQueue2Stack(unittest.TestCase):
    
    def test_empty_queue(self):
        queue = Queue2Stack()
        self.assertEqual(len(queue), 0, "should be empty")

    def test_push_queue(self):
        queue = Queue2Stack()
        queue.push("hello")
        queue.push("world")
        self.assertEqual(len(queue), 2, "length of 'hello' and 'world' should be 2")

    def test_pop_queue(self):
       queue = Queue2Stack()
       queue.push("hello")
       queue.push("world") 
       self.assertEqual(len(queue), 2)
       self.assertEqual(queue.pop(), "hello")
       self.assertEqual(len(queue), 1)
       queue.push("fly")
       queue.push("to")
       queue.push("the")
       queue.push("moon")
       self.assertEqual(len(queue), 5)
       self.assertEqual(queue.pop(), "world")
       self.assertEqual(len(queue), 4)
       self.assertEqual(queue.pop(), "fly")
       self.assertEqual(len(queue), 3)

if __name__ == "__main__":
    unittest.main()