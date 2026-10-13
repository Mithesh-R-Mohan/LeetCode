class Solution(object):
    def wordPattern(self, pattern, s):
        w = s.split()
        if len(pattern) != len(w):
            return False
        checker = {}
        used = set()
        for c, d in zip(pattern, w):
            if c in checker:
                if checker[c] != d:
                    return False
            else:
                if d in used:
                    return False
                checker[c] = d
                used.add(d)
        return True