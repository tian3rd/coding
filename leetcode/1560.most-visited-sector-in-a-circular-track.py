#
# @lc app=leetcode id=1560 lang=python3
#
# [1560] Most Visited Sector in  a Circular Track
#

# @lc code=start
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        dic = {key: 0 for key in range(1, n+1)}
        dic[rounds[0]] += 1
        for r in range(1, len(rounds)):
            if rounds[r-1] > rounds[r]:
                rounds[r] += n
            for i in range(rounds[r-1]+1, rounds[r]+1):
                if i > n:
                    dic[i-n] += 1
                    continue
                dic[i] += 1
            if rounds[r] > n:
                rounds[r] -= n
        # rtn = {key: value for key, value in sorted(dic.items(), key=lambda item: item[1])}
        maxi = max(dic.values())
        rtn = []
        for i in range(1, n+1):
            if dic[i] == maxi:
                rtn.append(i)
        return rtn
        
# @lc code=end

