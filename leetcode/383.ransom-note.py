#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ran_dic = self.count_letters(ransomNote)
        mag_dic = self.count_letters(magazine)
        if len(ran_dic.keys()) > len(mag_dic.keys()):
            return False
        for letter in ran_dic.keys():
            if letter not in mag_dic.keys() or ran_dic[letter] > mag_dic[letter]:
                return False
        return True

    def count_letters(self, s: str) -> Dict:
        dic = dict()
        for i in range(len(s)):
            if s[i] not in dic.keys():
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        # print(dic)
        return dic

        
# @lc code=end

