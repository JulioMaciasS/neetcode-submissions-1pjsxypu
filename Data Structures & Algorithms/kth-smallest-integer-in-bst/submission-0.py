# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
   
        if not root:
            return -1
            
        nodesList = []
        def dfs(node):
            if not node:
                return node
            nodesList.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return node
        # All values will be added to a list
        dfs(root)
        nodesList = sorted(nodesList)
        return nodesList[k-1]

        