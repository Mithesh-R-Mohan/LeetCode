class Solution(object):
    def findDisappearedNumbers(self, nums):
        s=set(nums)
        m=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                m.append(i)
        return m