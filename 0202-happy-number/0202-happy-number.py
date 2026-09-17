class Solution:
    def isHappy(self, n):
        checked = set()
        while n!=1 and n not in checked:
            checked.add(n)
            n = sum(int(d) ** 2 for d in str(n))    
        return n == 1