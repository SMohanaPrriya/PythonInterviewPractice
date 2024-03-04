"""
Input: Two strings s and t
Output: True, if t is an anagram of s
        False, otherwise
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_s[t[i]] = count_s.get(t[i], 0) - 1

        for key in count_s:
            if count_s[key] != 0:
                return False
        return True


s = Solution()
print(s.isAnagram('car', 'rac'))
print(s.isAnagram('cart', 'rac'))
print(s.isAnagram('anagram', 'nagaram'))
