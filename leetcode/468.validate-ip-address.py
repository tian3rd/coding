#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#

# @lc code=start
class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(IP: str) -> bool:
            arr = IP.split(".")
            if len(arr) != 4:
                return False
            for add in arr:
                if not add.isnumeric():
                    return False
                if int(add) > 255:
                    return False
                # check leading 0s
                if add != str(int(add)):
                    return False
            return True
        
        def isIPv6(IP: str) -> bool:
            setvalid = set([str(i) for i in range(10)])
            setvalid = setvalid.union(set([chr(i) for i in range(ord('a'), ord('g'))] \
                +([chr(i) for i in range(ord('A'), ord('G'))])))
            arr = IP.split(":")
            if len(arr) != 8:
                return False
            for add in arr:
                if len(add) < 1 or len(add) > 4:
                    return False
                for c in add:
                    if c not in setvalid:
                        return False
            return True
        if isIPv4(IP):
            return "IPv4"
        if isIPv6(IP):
            return "IPv6"
        return "Neither"
                
# @lc code=end

