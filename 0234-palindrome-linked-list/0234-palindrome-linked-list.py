# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        t,l=head,[]
        while t:
            l.append(t.val)
            t=t.next
        for i in range(len(l)//2):
            if l[i]!=l[-i-1]:
                return False
        return True