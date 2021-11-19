#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # rtn = []
        # def permutation(nums, start, end):
        #     if start == end:
        #         rtn.append(nums)
        #         return
        #     for i in range(start, end+1):
        #         nums[start], nums[i] = nums[i], nums[start]
        #         # why permutations(nums, start+1, end) does not work?
        #         permutation(nums[:], start+1, end)
        #         nums[start], nums[i] = nums[i], nums[start]
        # permutation(nums, 0, n-1)
        # return rtn

        # 2nd try: 
        rtn = []
        def backtrack(path, choices):
            # if there's not choices left, then the path is complete
            if not choices:
                # do a full copy of the list to rtn, rather than just add path (or it will change whenever path pops or appends)
                rtn.append(path[:])
                return
            for i in range(len(choices)):
                path.append(choices[i])
                # exclude the current choice from the choices to avoid duplicates
                backtrack(path, choices[:i] + choices[i+1:])
                path.pop()
        backtrack([], nums)
        return rtn


        
# @lc code=end

