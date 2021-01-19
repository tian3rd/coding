import unittest

def nearest_neighbors(lst: list) -> set: 
    rtn = set()
    mini = float('inf')
    lst.sort()
    for index in range(len(lst)-1):
        if lst[index+1] - lst[index] < mini:
            mini = lst[index+1] - lst[index]
            rtn = set([(lst[index], lst[index+1])])
        elif lst[index+1] - lst[index] == mini:
            rtn.add((lst[index], lst[index+1]))
    print(rtn)
    return rtn

class TestNN(unittest.TestCase):

    def test_nn(self):
        test1 = [2, 1, 0, -5]
        self.assertEqual(nearest_neighbors(test1), {(0,1),(1,2)})
        test2 = [0, 0, -1]
        self.assertEqual(nearest_neighbors(test2), {(0,0)})
    
if __name__ == "__main__":
    unittest.main()