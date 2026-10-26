from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        h = Counter(s)
        for i, ch in enumerate(s):
            if h[ch] == 1:
                return i
        return -1