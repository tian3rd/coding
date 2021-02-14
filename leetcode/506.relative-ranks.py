#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = score[:]
        rank = sorted(rank)
        rtn = []
        dic = dict()
        if len(rank) == 1:
            dic[rank[0]] = "Gold Medal"
        elif len(rank) == 2:
            dic[rank[-1]] = "Gold Medal"
            dic[rank[-2]] = "Silver Medal"
        else:
            dic[rank[-1]] = "Gold Medal"
            dic[rank[-2]] = "Silver Medal"
            dic[rank[-3]] = "Bronze Medal"
            for i in range(len(rank)-3):
                dic[rank[i]] = str(len(rank)-i)
        for s in score:
            rtn.append(dic[s])
        return rtn 

# @lc code=end

