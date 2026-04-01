# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        nodes = []
        currNode = head
        while currNode:
            nodes.append(currNode)
            currNode = currNode.next
        
        p1 = 0
        p2 = len(nodes)-1

        while p1 < p2:
            nodes[p1].next = nodes[p2]
            p1+=1
            if p1 >= p2:
                break
            nodes[p2].next = nodes[p1]
            p2-=1
        nodes[p2].next = None




 
