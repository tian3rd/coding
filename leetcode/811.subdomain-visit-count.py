#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#

# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        rtn = dict()
        for dom in cpdomains:
            cnt, full = dom.split(" ")
            # convert to integer
            cnt = int(cnt)
            # find indices of all . add first dot to the front
            indice = [-1] + [i for i in range(len(full)) if full[i]=='.']
            for i in indice:
                # +1 omit the .
                if full[i+1:] not in rtn:
                    rtn[full[i+1:]] = cnt
                else:
                    rtn[full[i+1:]] += cnt
        return [str(v)+" "+k for k,v in rtn.items()]
        
# @lc code=end

