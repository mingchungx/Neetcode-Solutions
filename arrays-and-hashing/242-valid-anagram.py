class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # We can compare their letters and how many times they appear
        s = {i: s.count(i) for i in s}
        t = {i: t.count(i) for i in t}
        return s == t