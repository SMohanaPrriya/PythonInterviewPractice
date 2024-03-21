class Solution:

    def encode(self, strs: list[str]) -> str:
        return ''.join(str(len(i)) + '#' + i for i in strs)

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            i = j + 1 + int(s[i:j])
            res.append(s[j + 1:i])
        return res
