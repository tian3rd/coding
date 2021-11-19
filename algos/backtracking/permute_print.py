import unittest

def permute(nums):
    rtn = []
    def backtrack(path, choices):
        if not choices:
            rtn.append(path[:])
            return
        for i in range(len(choices)):
            path.append(choices[i])
            backtrack(path, choices[:i] + choices[i+1:])
            path.pop() 
    backtrack([], nums)
    return rtn

class TestPermute(unittest.TestCase):
    def test_permute(self):
        self.assertEqual(permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

if __name__ == "__main__":
    unittest.main()