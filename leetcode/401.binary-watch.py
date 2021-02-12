#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = {key: bin(key).count("1") for key in range(12)}
        minutes = {key: bin(key).count("1") for key in range(60)}
        rtn = []
        for h in hours:
            for m in minutes:
                if hours[h]+minutes[m] == num:
                    rtn.append("{}:{}".format(str(h), str(m) if m>9 else "0"+str(m)))
        return rtn
        
# @lc code=end

