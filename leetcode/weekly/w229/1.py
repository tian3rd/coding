class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # word1 = list(word1)
        # word2 = list(word2)
        lmin = min(len(word1), len(word2))
        # lmax = max(len(word1), len(word2))
        rtn = ''
        
        for i in range(lmin):
            rtn += word1[i]+word2[i]
        if len(word1)<len(word2):
            rtn += word2[lmin:]
        else:
            rtn += word1[lmin:]
        return rtn
        


