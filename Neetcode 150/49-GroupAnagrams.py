from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        diff = defaultdict(list)
        for s in strs:
            count = [0] * 26 #a...z
            for c in s:
                count[ord(c)-ord("a")]+=1
            diff[tuple(count)].append(s)
        return diff.values()