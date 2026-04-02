# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxDepth = 0
        q = deque()
        q.append((root, 0))

        while 0<len(q):
            curr, depth = q.popleft()
            depth += 1
            maxDepth = max(depth, maxDepth)
            if curr and curr.left:
                q.append((curr.left, depth))
            if curr and curr.right:
                q.append((curr.right,depth))
        return maxDepth        
        

