#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def one_move(cur: str) -> List[str]:
            rtn = []
            for i in range(len(cur)):
                rtn.append(cur[:i] + str((int(cur[i]) + 1) % 10) + cur[i+1:])
                rtn.append(cur[:i] + str((int(cur[i]) + 9) % 10) + cur[i+1:])
            return rtn

        q = collections.deque()
        visited = set()
        q.append('0000')
        visited.add('0000')
        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur == target:
                    return step
                # if deadend, skip it for next possible move
                if cur in deadends:
                    continue
                for next_code in one_move(cur):
                    # can't do all checks in here like this: if next_code not in visited and next_code not in deadends:
                    # only check to avoid duplicates
                    if next_code not in visited:
                        q.append(next_code)
                        visited.add(next_code)
            step += 1
        return -1
        
        
# @lc code=end

