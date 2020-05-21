# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
		 def _helper_alt(node, L, R):
            res = []
            if not node:
                return res
            if node.val >= L and node.val <= R:
                res.append(node.val)
            return _helper(node.left) + res + _helper(node.right)

          return sum(_helper_alt(root, L, R))