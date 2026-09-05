class Solution(object):
    def titleToNumber(self, c):
        n = 0
        for i in c:
            n = n * 26 + (ord(i) - 64)
        return n