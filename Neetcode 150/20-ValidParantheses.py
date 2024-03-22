class Solution:
    def isvalid(self, s: str) -> bool:
        st = {"]": "[", "}": "{", ")":"("}
        a = []
        for c in s:
            if c in st:
                if len(a) == 0 or a.pop() != st.get(c):
                    return False
            else:
                a.append(c)
        return True if len(a) == 0 else False
