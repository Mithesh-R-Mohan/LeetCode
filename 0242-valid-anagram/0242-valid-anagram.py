class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for i in t:
            if i not in h:
                return False
            else:
                h[i]-=1
                if h[i]==-1:
                    return False
        return True