# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
solution=Solution()
root=TreeNode(5)
root.left=TreeNode(4)
root.right=TreeNode(8)
root.left.left=TreeNode(11)
root.right.left=TreeNode(13)
root.right.right=TreeNode(4)
root.left.left.left=TreeNode(7)
root.left.left.right=TreeNode(2)
root.right.right.right=TreeNode(1)
print solution.hasPathSum(root,21)
