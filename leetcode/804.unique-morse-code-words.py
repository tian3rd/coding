#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        diffmorses = set()
        for word in words:
            morse = ''
            for letter in word:
                morse += morses[ord(letter)-ord('a')]
            diffmorses.add(morse)
        return len(diffmorses)
        
# @lc code=end

