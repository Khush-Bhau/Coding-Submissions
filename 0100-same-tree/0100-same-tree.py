# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # Case 1: Both nodes are None (structural match at the leaf)
        if not p and not q:
            return True
        
        # Case 2: One node is None but the other is not (structural mismatch)
        if not p or not q:
            return False
        
        # Case 3: Both nodes exist, but values are different
        if p.val != q.val:
            return False
        
        # Case 4: Current nodes match, recurse on children
        # Both left subtrees must match AND both right subtrees must match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)