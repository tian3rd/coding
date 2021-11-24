#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        rtn = []
        def backtrack(path, choices):
            if len(path) == k:
                rtn.append(path[:])
                return
            for choice in choices:
                if 0 < len(path) and len(path) < k and choice <= path[-1]:
                    continue
                path.append(choice)
                backtrack(path, choices)
                path.pop()
        backtrack([], list(range(1, n+1)))
        return rtn
        
# @lc code=end

