# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # If root is null, return None
        if not root:
            return None
        
        # Swap the children of the current root
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # Use recursion to swap subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
        # Can use recursion to invert Binary Tree
        # Use Depth First Search:
        # DFS: Traverse left subtree first, then the right subtree
        
        # Passing root node
        # Return invert tree starting from node