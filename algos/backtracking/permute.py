class permute:
    def __init__(self, lst: list):
        self.lst = list(lst)
        self.rtn = []
    
    def generate(self):
        start, end = 0, len(self.lst)-1

        def permute(start: int, end: int):
            if start == end:
                self.rtn.append(''.join(self.lst))
                return
            for i in range(start, end+1):
                self.lst[start], self.lst[i] = self.lst[i], self.lst[start]
                permute(start+1, end)
                self.lst[start], self.lst[i] = self.lst[i], self.lst[start]

        permute(start, end)
        return self.rtn

if __name__ == '__main__':
    test = permute("abcde")
    print(len(test.generate()))