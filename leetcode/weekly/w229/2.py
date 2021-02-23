class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        rtn = []
        balls = [i for i in range(len(boxes)) if boxes[i]=='1']
        for i in range(len(boxes)):
            rtn.append(sum([abs(balls[j]-i) for j in range(len(balls))]))
        return rtn


